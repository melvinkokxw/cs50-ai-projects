import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to" | "until"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | S Conj S | S P S
NP -> N | Det AdjN | NP PNP
VP -> V | V NP | VP PNP | VP Adv | Adv VP | VP Conj VP
AdjN -> N | Adj AdjN
PNP -> P NP
"""


grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    sentence = sentence.lower()
    words = nltk.word_tokenize(sentence)
    for word in words.copy():
        if not any(c.isalpha() for c in word):
            words.remove(word)
    return words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks = []

    # Recursively search for "NP" in a subtree
    def search_np(subtree):
        # If at height 2 i.e. the end, check if it is NP
        if subtree.height() == 2:
            return subtree.label() == "NP"
        # Recursively search subtrees, except itself
        for sub in subtree.subtrees(lambda t: t != subtree):
            if sub.label() == "NP":
                return True
            if search_np(sub):
                return True
        return False

    # For all subtrees labelled "NP",
    # if subtree does not have another subtree labelled "NP" within it,
    # append to np chunks
    for sub in tree.subtrees(lambda t: t.label() == "NP"):
        if not search_np(sub):
            chunks.append(sub)

    return chunks


if __name__ == "__main__":
    main()
