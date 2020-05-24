# Week 6: Language <!-- omit in toc -->

- [Syntax](#syntax)
  - [Formal grammer](#formal-grammer)
    - [Context-free grammer](#context-free-grammer)
  - [n-gram](#n-gram)
  - [Tokenisation](#tokenisation)
- [Text Categorisation](#text-categorisation)
  - [Bag-of-words model](#bag-of-words-model)
  - [Naive Bayes](#naive-bayes)
    - [Additive smoothing](#additive-smoothing)
    - [Laplace smoothing](#laplace-smoothing)
- [Information retrieval](#information-retrieval)
  - [Topic modeling](#topic-modeling)
  - [Term frequency](#term-frequency)
  - [Function words](#function-words)
  - [Content words](#content-words)
  - [Inverse document frequency](#inverse-document-frequency)
  - [TF-IDF](#tf-idf)
- [Semantics](#semantics)
  - [Information extraction](#information-extraction)
  - [One-hot representation](#one-hot-representation)
  - [Distribution representation](#distribution-representation)
  - [word2vec](#word2vec)
  - [Skip-gram architecture](#skip-gram-architecture)

# Syntax

Structure of language and how is it that that structure works

## Formal grammer

A system of rules for generating sentences in a language

### Context-free grammer

Replacing non-terminal symbols whether terminal symbols based on a set of rules

Examples of non-terminal symbols:
Symbol | Meaning | Examples
-------|-------- | --------
N | Noun | she, city, car, Harry
D | Determiner | the, a, an
V | Verb | saw, ate, walked
P | Preposition | to, on , over
ADJ | Adjective | blue, busy, old
NP | Noun Phrase | N or D N
VP | Verb Phrase | V or V NP
S | Sentence | NP VP

## n-gram

A contiguous sequence of n items from a sample of text

Type | Definition
-----|-----------
Character n-gram | A contiguous sequence of n characters from a sample of text
Word n-gram | A contiguous sequence of n words from a sample of text
Unigram | A contiguous sequence of 1 item from a sample of text
Bigram | A contiguous sequence of 2 item from a sample of text
Trigram | A contiguous sequence of 3 item from a sample of text

## Tokenisation

The task of splitting a sequence of characters into pieces (tokens)

Type | Definition
-----|-----------
Word tokenization | The task of splitting a sequence of characters into words
Sentence tokenization | The task of splitting a sequence of characters into sentences

# Text Categorisation

## Bag-of-words model

Model that represents text as an unordered collection of words

## Naive Bayes

Naive Bayes is an application of the Bayes theorem to classify word. However, an assumption is made (hence `naïve`), that is we assume that every feature is independent from one another.

However, one siginificant problem  with the Naive Bayes approach is that if any feature has a probability of 0, the calculated probability with also be 0, which is inaccurate.

### Additive smoothing

Adding a value `α` to each value in our distribution to smooth the data. One of type of this is Laplace smoothing.

### Laplace smoothing

Adding 1 to each value in our distribution: pretending we've seen each value one more time than we actually have

# Information retrieval

The task of finding relevant documents in response to a user query

## Topic modeling

Models for discovering the topics for a set of documents

## Term frequency

Number of times a term appears in a document

## Function words

Words that have little meaning on their own, but are used to grammatically connect other words. E.g. am, by, do, is, which, with, yet, ...

## Content words

Words that carry meaning independently. E.g. algorithm, category, computer, ...

## Inverse document frequency

Measure of how common or rare a word is across documents

![{log}\frac{TotalDocuments}{NumDocumentsContaining(word)}](https://render.githubusercontent.com/render/math?math=%7Blog%7D%5Cfrac%7BTotalDocuments%7D%7BNumDocumentsContaining(word)%7D)

## TF-IDF

Rankinf of what words are important in a document by multiplying [term frequency](#term-frequency)(TF) by [inverse document frequency](#inverse-document-frequency)(IDF)

# Semantics

What a word or sequence of words mean

## Information extraction

The task of extracting knowledge from documents

## One-hot representation

Representation of meaning as a vector with a single 1, and with other values as 0

## Distribution representation

Representation of meaning distributed across multiple values

## word2vec

Model for generating word vectors

## Skip-gram architecture

Neural network architecture for predicting context words given a target word