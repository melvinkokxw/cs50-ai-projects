import nltk
import sys
import os
import string
import math

FILE_MATCHES = 3
SENTENCE_MATCHES = 3


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    contents = {}
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename)) as file:
            contents[filename] = file.read()
    return contents


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    # Remove punctuation and change to lowercase
    clean_string = document.lower().translate(str.maketrans("", "", string.punctuation))
    # Split words into list
    contents = nltk.word_tokenize(clean_string)
    # Remove stopwords
    for item in contents.copy():
        if item in nltk.corpus.stopwords.words("english"):
            contents.remove(item)

    return contents


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    # Create empty set of words
    words = set()
    # Add all words in documents to set
    for document in documents:
        words.update(documents[document])
    # Create idf dictionary with words as keys
    idfs = dict.fromkeys(words, 0)
    # Check each word if word in documents
    for word in words:
        for document in documents:
            if word in documents[document]:
                idfs[word] += 1
    # Compute idf
    for word in idfs:
        idfs[word] = math.log(len(documents) / idfs[word])
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    def tfidf_calc(word, file):
        words = files[file]
        if word in words:
            tf = words.count(word) / len(words)
            idf = idfs[word]
            return tf * idf
        return 0

    # Create dictionary of scores
    scores = dict.fromkeys(files.keys(), 0)
    # Get scores for each document
    for file in scores:
        for word in query:
            scores[file] += tfidf_calc(word, file)

    top = []
    # Get top files
    for i in range(n):
        file = max(scores, key=scores.get)
        top.append(file)
        scores.pop(file)

    return top


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """

    def get_qtd(sentence):
        qtd = 0
        for word in sentence:
            if word in query:
                qtd += 1
        qtd /= len(sentence)
        return qtd

    scores = []
    for sentence in sentences:
        # Get idf value
        idf = 0
        for word in query:
            if word in sentences[sentence]:
                idf += idfs[word]

        # Get query term density
        qtd = get_qtd(sentences[sentence])

        # Add data to list as tuple
        scores.append((sentence, idf, qtd))

    # Sort scores according to idf, then qtd
    scores.sort(key=lambda x: (x[1], x[2]), reverse=True)

    # Return top n sentences
    top = []
    for i in range(n):
        top.append(scores[i][0])
    return top


if __name__ == "__main__":
    main()
