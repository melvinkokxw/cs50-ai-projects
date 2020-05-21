# Week 4: Learning <!-- omit in toc -->

- [Supervised learning](#supervised-learning)
  - [Classification](#classification)
    - [Nearest-neighbour classification](#nearest-neighbour-classification)
    - [Perceptron learning rule](#perceptron-learning-rule)
  - [Support Vector Machines](#support-vector-machines)
    - [Maximum margin separator](#maximum-margin-separator)
  - [Regression](#regression)
  - [Loss function](#loss-function)
    - [0-1 loss function](#0-1-loss-function)
    - [L1 loss function](#l1-loss-function)
    - [L2 loss function](#l2-loss-function)
  - [Overfitting](#overfitting)
    - [Regularization](#regularization)
    - [Holdout cross-validation](#holdout-cross-validation)
    - [K-fold cross-validation](#k-fold-cross-validation)
- [Reinforcement learning](#reinforcement-learning)
  - [Markov Decision Process](#markov-decision-process)
  - [Q-learning](#q-learning)
    - [Overview](#overview)
    - [Algorithm](#algorithm)
    - [Greedy decision-making](#greedy-decision-making)
    - [ε-greedy](#ε-greedy)
- [Unsupervised learning](#unsupervised-learning)
  - [Clustering](#clustering)
    - [k-means clustering](#k-means-clustering)

# Supervised learning

Given a data set of input-output pairs, learn a function to map inputs to outputs

## Classification

Supervised learning task of learning a function mapping an input point to discrete category

### Nearest-neighbour classification

1-nearest-neighbour classification:

* Algorithm that, given an input, chooses the class of the nearest data point to that input

k-nearest-neighbour classification:

* Algorithm that, given an input, chooses the most common class out of the *k* nearest data points to that input.

![h_\mathbf{w}(\mathbf{x})= \begin{cases} 1, & \text{if}\ \mathbf{w} \cdot \mathbf{x} \geq 0 \\ 0, & \text{otherwise} \end{cases}](https://render.githubusercontent.com/render/math?math=h_%5Cmathbf%7Bw%7D(%5Cmathbf%7Bx%7D)%3D%20%5Cbegin%7Bcases%7D%201%2C%20%26%20%5Ctext%7Bif%7D%5C%20%5Cmathbf%7Bw%7D%20%5Ccdot%20%5Cmathbf%7Bx%7D%20%5Cgeq%200%20%5C%5C%200%2C%20%26%20%5Ctext%7Botherwise%7D%20%5Cend%7Bcases%7D)

### Perceptron learning rule

Given data point (x, y), update each weight according to:

<pre><code>w<sub>i</sub> = w<sub>i</sub> + α(y - h<sub><b>w</b></sub>(<b>x</b>)) × x<sub>i</sub></code></pre>

## Support Vector Machines

### Maximum margin separator

Boundary that maximises the distance between any of the data points

## Regression

Supervised learning task of learning a function mapping an input point to a continuous value

## Loss function

Function that expresses how poorly our hypothesis performs

### 0-1 loss function

```
L(actual, predicted) = 
    0 if actual = predicted
    1 otherwise
```

### L1 loss function

```
L(actual, predicted) = |actual - predicted|
```

### L2 loss function

<pre><code>L(actual, predicted) = (actual - predicted)<sup>2</sup></code></pre>

## Overfitting

An overfitted model is one that fits too closely to a particular data set and therefore may fail to generalise to future data

### Regularization

To avoid overfitting, we can use regularisation. Regularisation refers to penalizing hypotheses that are more complex to favor simpler, more general hypotheses.

```
cost(h) = loss(h) + λcomplexity(h)
```

### Holdout cross-validation

Splitting data into a training set and a test set, such that learning happens on the training set and is evaluated on the test set.

### K-fold cross-validation

Splitting data into k sets, and experimenting k times, using each set as a test set once, and using remaining data as training set

# Reinforcement learning

Given a set of rewards and punishments, learn what actions to take in the future

## Markov Decision Process

Model for decision-making, representing states, actions and their rewards

* Set of states `S`
* Set of actions `ACTIONS(s)`
* Transition model `P(s'|s, a)`
* Reward function `R(s, a, s')`

## Q-learning

Method for learning a function `Q(s, a)`, estimate of the value of performing action `a` in state `s`

### Overview

* Start with `Q(s, a)` = 0 for all `s, a`
* When we taken an action and receive a reward:
  * Estimate the value of `Q(s, a)` based on current reward and expected future rewards
  * Update `Q(s, a)` to take into account old estimate as well as our new estimate

### Algorithm

* Start with `Q(s, a) = 0` for all `s, a`
* Every time we take an action a in state s and observe a reward r, we update:

<pre><code>Q(s, a) ← Q(s, a) + α((r + γmax<sub>a'</sub>Q(s', a')) - Q(s, a))</code></pre>

### Greedy decision-making

When in state `s`, choose action `a` with highest `Q(s, a)`

### ε-greedy

* Set `ε` equal to how often we want to move randomly
* With probability `1 - ε`, choose estimated best move
* With probability `ε`, choose a random move

# Unsupervised learning

Given input data without any additional feedback, learn patterns

## Clustering

Organising a set of objects into groups in such a way that similar objects tend to be in the same group

### k-means clustering

Algorithm for clustering data based on repeatedly assigning points to clusters and updating those clusters' centers