# Week 3: Optimization <!-- omit in toc -->

- [Local search](#local-search)
  - [State-space landscape](#state-space-landscape)
  - [Hill-climbing](#hill-climbing)
  - [Simulated annealing](#simulated-annealing)
  - [Linear Programming](#linear-programming)

# Local search

Local search refers to earch algorithms that maintain a single node and searches by moving to a neighbouring node. 

Unlike previous search algorithms like DFS or BFS where finding a path to a known goal state is the main problem, local search is used where finding the goal state is the main problem.

## State-space landscape

The state-space landscape is the distribution of values given by either the objective or cost function.

The objective function returns the utility of a state for our problem given a state, while the cost function returns the cost of a state for our problem given a state.

The objective function is associated when we are looking for a global maximum in our state-space landscape, while cost function is used when looking for the global minimum.

## Hill-climbing

* Start from an initial state
* Repeat indefinitely:
    * Find highest valued neighbour of current state
    * If neighbour is not better than current state:
        * Return current state
    * Else set current state to the highest valued neighbour

Basic hill-climbing algorithm only gives local maxima/minima, so variants exist to solve the problem:


| Variant           | Definition                                    |
| ----------------- | --------------------------------------------- |
| steepest-ascent   | choose the highest-valued neighbour           |
| stochastic        | choose randomly from higher-valued neighbours |
| first-choice      | choose the first higher-valued neighbour      |
| random-restart    | conduct himm climbing multiple times          |
| local beam search | chooses the k highest-valued neighbours       |

## Simulated annealing

* Set current state = initial state
* Repeat for specified number of times:
    * Get current "temperature", `T`
    * Pick random neighbour of current state
    * Get `ΔE`, i.e. how much better neighbour is than current
    * If `ΔE` > 0:
        * Set current state = neighbour
    * Else with probability <code>e<sup>ΔE/T</sup></code> set current = neighbour

Allows for a neighbour with lower utility to be chosen, with probability based on `ΔE` and `T`.

