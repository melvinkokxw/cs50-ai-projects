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
- [Adjustments to Keras model](#adjustments-to-keras-model)
  - [Different numbers of convolutional and pooling layers](#different-numbers-of-convolutional-and-pooling-layers)
    - [Number of convolution layers](#number-of-convolution-layers)
    - [Number of pooling layers](#number-of-pooling-layers)
  - [Different numbers and sizes of filters for convolutional layers](#different-numbers-and-sizes-of-filters-for-convolutional-layers)
    - [Number of filters](#number-of-filters)
    - [Sizes of filters](#sizes-of-filters)
  - [Different pool sizes for pooling layers](#different-pool-sizes-for-pooling-layers)
  - [Different numbers and sizes of hidden layers](#different-numbers-and-sizes-of-hidden-layers)
  - [Dropout](#dropout-1)

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

# Adjustments to Keras model

By changing the number of layers and the types of layers in the Keras, I got different results from the project5 traffic data.

## Different numbers of convolutional and pooling layers

This was testing by varying the number of layers from 0-2.

### Number of convolution layers

Increasing the number of convolution layers increases the accuracy and reduces the loss of the model. However, each layer adds to the amount of time required to train the model as well as the computational power required.

### Number of pooling layers

Increasing the number of pooling layers decreases the time required to train the model, but decreases the accuracy of the model.

## Different numbers and sizes of filters for convolutional layers

The effect of number of filters was tested with 1, 16 and 32 filters. The effect of sizes of filters was tested with 3x3, 5x5 and 7x7.

### Number of filters

Increasing the number of filters from 1 to 16 increases the accuracy of the model. However, increasing from 16 to 32 filters had little effect on the accuracy of the model, while increasing the amount of time required to run significantly (2x).

### Sizes of filters

Using small sized filters generally increases accuracy, though larger sized filters can be used to learn larger features on larger images.

## Different pool sizes for pooling layers

Increasing pool size has a similar effect to increasing number of pool layers – decreasing amount of time taken to fit the model but also decreasing accuracy.

## Different numbers and sizes of hidden layers

Only using one hidden layer significantly reduced accuracy and increased loss. However, continuing to add hidden layers increases the accuracy and decreases the loss, eventually reaching better results than without hidden layers.

## Dropout

Dropout reduces the effect of overfitting.