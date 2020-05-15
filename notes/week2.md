# Week 2: Uncertainty

Often we deal with uncertainty when we implement AIs. While the AI may not be certain about an event, it likely has access to the probabilities of the events occuring.

# Probability

The symbol `ω` represents a possible world, e.g. when we roll a die there are 6 possible worlds. `P(ω)` represents the probability of the world being true. The probability of an event lies between 0 and 1, i.e. `0 ≤ P(ω) ≤ 1`, where a probability of 0 represents that the event will never happen while a probability of 1 represents that the event will always happen. For all the possible worlds, if we add up their probability, the sum is 1, i.e. 

![\displaystyle\sum_{\omega\in\Omega} P(\omega) = 1](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle%5Csum_%7B%5Comega%5Cin%5COmega%7D%20P(%5Comega)%20%3D%201)

## Unconditional probability

Unconditional probability is the degree of belief in a proposition in the absence of any other evidence.

## Conditional probability

Conditional probability is the degree of belief in a proposition given some evidence that has already been revealed. This is more common when using AIs as we often use a knowledge base.

An example of conditional probability is `P(a|b)`. `P(a|b)` represents that probability of `a` given `b` is true. The calculation is given by:

![P(\textit{a}{\mid}\textit{b}) = \frac{P(a \land b)}{P(b)}](https://render.githubusercontent.com/render/math?math=P(%5Ctextit%7Ba%7D%7B%5Cmid%7D%5Ctextit%7Bb%7D)%20%3D%20%5Cfrac%7BP(a%20%5Cland%20b)%7D%7BP(b)%7D)

which can also be expressed as

```
P(a∧b) = P(a)P(b|a)
```

or

```
P(a∧b) = P(b)P(a|b)
```

## Random variable

A random variable is a variable in probability theory with a domain of possible values it can take on, e.g. when rolling a dice, there may be a random variable named `Roll` with the domain of `{1, 2, 3, 4, 5, 6}`. Each possible may have a different probability. The probability of each value is given by a probability distribution.

Probability distributions can be expressed in different ways. For example, if a flight has three probable states – on time, delayed and cancelled, the probability distribution can be expressed this way:

```
P(Flight = on time) = 0.6
P(Flight = delayede) = 0.3
P(Flight = cancelled) = 0.1
```

Alternatively, it can be expressed more concisely in this way:

<pre><b>P</b>(Flight) = <0.6, 0.3, 0.1></pre>

but we will have to know the order in which the probabilities are arranged.

## Independance

Independance refers to the knowledge that one event occurs does not affect the probability of the other event, i.e. one event does not influence another. Independence is represented mathematically with:

```
P(a∧b) = P(a)P(b)
```

## Bayes' Rule

From `P(a∧b) = P(a)P(b|a)` and `P(a∧b) = P(b)P(a|b)`, we can get `P(a)P(b|a) = P(b)P(a|b)`. Rearranging the terms, we get:

![P(\textit{b}{\mid}\textit{a}) = \frac{P(\textit{a}{\mid}\textit{b})P(\textit{b})}{P(\textit{a})}](https://render.githubusercontent.com/render/math?math=P(%5Ctextit%7Bb%7D%7B%5Cmid%7D%5Ctextit%7Ba%7D)%20%3D%20%5Cfrac%7BP(%5Ctextit%7Ba%7D%7B%5Cmid%7D%5Ctextit%7Bb%7D)P(%5Ctextit%7Bb%7D)%7D%7BP(%5Ctextit%7Ba%7D)%7D)

Using Bayes' Rule, we can get the probability of `b` given `a` if we have the "reverse" conditional probability of `a` given `b`

## Negation

The probability of an event not occuring is equal to 1 minus the probability of the event happening, i.e.

```
P(¬a) = 1 P(a)
```

## Inclusion-Exclusion

Given two events `a` and `b`, the probably that either `a` or `b` occurs is given by:

```
P(a∨b) = P(a) + P(b) - P(a∧b)
```

Simply adding `P(a)` and `P(b)` causes double counting, which is which is why we have to exclude `P(a∧b)`.

## Marginalization

The probability of `a` is the sum of:
* The probability of both `a`  and `b` occuring
* The probability of `a` occuring and `b` not occuring, i.e.

```
P(a) = P(a,b) + P(a,¬b)
```

For random variables, a more general equation would be:

![P(\textit{X} = \textit{x_{i}}) = \displaystyle\sum_{j}P(\textit{X} = \textit{x_{i}}, \textit{Y} = \textit{y_{j}})](https://render.githubusercontent.com/render/math?math=P(%5Ctextit%7BX%7D%20%3D%20%5Ctextit%7Bx_%7Bi%7D%7D)%20%3D%20%5Cdisplaystyle%5Csum_%7Bj%7DP(%5Ctextit%7BX%7D%20%3D%20%5Ctextit%7Bx_%7Bi%7D%7D%2C%20%5Ctextit%7BY%7D%20%3D%20%5Ctextit%7By_%7Bj%7D%7D))

I.e. the probability of that some random variable `X` is equal to <code>x<sub>i</sub></code> is the sum of the probabilities that <code>X = x<sub>i</sub></code> and <code>Y = y<sub>j</sub></code>, for all `j`.

## Conditioning 

The probability of `a` is the sum of:
* The probability of `a` occuring given that `b` occured, assuming `b` occured
* The probability of `a` occuring given that `b` did not occur, assuming `b` did not occur

In mathematical terms:

```
P(a) = P(a|b)P(b) + P(a|¬b)P(¬b)
```

This can be derived from the [marginalization](#marginalization) equation and the basic [conditional probability](#conditional-probability) equation

General equation for random variables:

![P(\textit{X} = \textit{x_{i}}) = \displaystyle\sum_{j}P(\textit{X} = \textit{x_{i}}{\mid}\textit{Y} = \textit{y_{j}})P(\textit{Y} = \textit{y_{j}})](https://render.githubusercontent.com/render/math?math=P(%5Ctextit%7BX%7D%20%3D%20%5Ctextit%7Bx_%7Bi%7D%7D)%20%3D%20%5Cdisplaystyle%5Csum_%7Bj%7DP(%5Ctextit%7BX%7D%20%3D%20%5Ctextit%7Bx_%7Bi%7D%7D%7B%5Cmid%7D%5Ctextit%7BY%7D%20%3D%20%5Ctextit%7By_%7Bj%7D%7D)P(%5Ctextit%7BY%7D%20%3D%20%5Ctextit%7By_%7Bj%7D%7D))

I.e. the probability that some random variable `X` is equal to <code>x<sub>i</sub></code> is the sum of the probabilities of <code>X = x<sub>i</sub></code> given <code>Y = y<sub>j</sub></code> for all `j`, assuming <code>Y = y<sub>j</sub></code> is true.

