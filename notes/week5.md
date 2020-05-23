# Week 5: Neural Networks <!-- omit in toc -->

- [Artificial neural networks](#artificial-neural-networks)
  - [Activation functions](#activation-functions)
  - [Gradient descent](#gradient-descent)
    - [Stochastic gradient descent](#stochastic-gradient-descent)
    - [Mini-batch gradient descent](#mini-batch-gradient-descent)
- [Multilayer neural network](#multilayer-neural-network)
  - [Backprogagation](#backprogagation)
  - [Deep neural networks](#deep-neural-networks)
  - [Dropout](#dropout)
- [Computer vision](#computer-vision)
  - [Image convolution](#image-convolution)
  - [Pooling](#pooling)
    - [Max-pooling](#max-pooling)
  - [Convolution neural network](#convolution-neural-network)
  - [Feed-forward neural network](#feed-forward-neural-network)
  - [Recurrent neural network](#recurrent-neural-network)

# Artificial neural networks

* Model mathematical function from inputs to ouputs based on the structure and parameters of the network
* Allows for learning the network's parameters based on data

## Activation functions

Function | Equation
---------|---------
Step function | g(x) = 1 if x ≥ 0, else 0
Logistic sigmoid | g(x) = e<sup>x</sup> / e<sup>x</sup> + 1
Rectified linear unit (ReLU) | g(x) = max(0, x)

## Gradient descent

Algorithm for minimizing loss when training neural network

* Start with a random choice of weights
* Repeat:
  * Calculate the gradient based on **all data points**: direction that will lead to decreasing loss
  * Update weights according to the gradient

### Stochastic gradient descent

* Start with a random choice of weights
* Repeat:
  * Calculate the gradient based on **one data point**: direction that will lead to decreasing loss
  * Update weights according to the gradient

### Mini-batch gradient descent

* Start with a random choice of weights
* Repeat:
  * Calculate the gradient based on **one small batch**: direction that will lead to decreasing loss
  * Update weights according to the gradient

# Multilayer neural network

Artifical neural network with an input layer, an output layer and at least one hidden layer

## Backprogagation

Algorithm for training neural networks with
hidden layers

* Start with a random choice of weights.
* Repeat:
  * Calculate error for output layer.
  * For each layer, starting with output layer, and moving inwards towards earliest hidden layer:
    * Propagate error back one layer.
    * Update weights

## Deep neural networks

Neural network with multiple hidden layers

## Dropout

Temporarily removing units — selected at
random — from a neural network to prevent
over-reliance on certain units

# Computer vision

Computational methods for analysing and
understanding digital images

## Image convolution

Applying a filter that adds each pixel value
of an image to its neighbors, weighted
according to a kernel matrix

## Pooling 

Reducing the size of an input by sampling from regions in the input

### Max-pooling

Pooling by choosing the maximum value in each region

## Convolution neural network

Neural networks that use convolution, usually for analysing images

General steps:

Convolution -> Pooling -> Flattening

We can repeat convolution and pooling multiple times

## Feed-forward neural network

Neural network that has connections only in one direction

## Recurrent neural network

Neural network that generates output that
feeds back into its own inputs