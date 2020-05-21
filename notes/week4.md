# Week 4: Learning <!-- omit in toc -->

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

<code>w<sub>i</sub> = w<sub>i</sub> + α(y - h<sub><b>w</b></sub>(<b>x</b>)) × x<sub>i</sub></code>

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

### L<sub>1</sub> loss function

```
L(actual, predicted) = |actual - predicted|
```

### L<sub>2</sub> loss function

<pre><code>L(actual, predicted) = (actual - predicted)<sup>2</sup></code></pre>

## Overfitting

A model that fits too closely to a particular data set and therefore may fail to generalise to future data