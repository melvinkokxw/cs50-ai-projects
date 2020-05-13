# Week 0: Search

A search problem is one where given an environment that an agent is in, we would like the agent to be able to somehow look for a solution to that problem. A search problem comes in many forms, common examples include:

* 15 puzzle with sliding tiles
* Tic-tac-toe
* Maze
* Getting directions in Google Maps

# Terminology

* **Agent**: An agent is an entity that perceives its environment and acts on that environment in some way.
* **State**: A state is some configuration of the agent in its environment.
    * Initial state: State where the agent begins in the problem/algorithm
* **Actions**: Choices available in any given state
* **Path cost**: Cost of any action taken 

# Implementation

The resulting implementation of agents, states and actions would be:

* Encode the states, e.g. in a numerical format.
    * E.g. for tic-tac-toe or sliding tile puzzle, each state is representated as a two-dimensional matrix
* Relate states and actions using a **transition model**
    * A transition model describes what state we get after performing some action on another state
    * Can be represented using a function with two inputs – the action and initial state
    * Function gives one output – the resultant state
* Form a **state space**, i.e. all the possible states we can get to from an initial state
    * Often represented as a graph with nodes and edges
    * Each node is a state and each edge is an action
* Create a **goal test** to determine if the AI is done with the problem
    * E.g. check if a goal state is reached
* Use **nodes** to keep track of actions
    * A node hold four pieces of information:
        * A state that the node represents
        * The node's parent node
        * The action taken to reach the node
        * The path cost from initial state to current state
    * Nodes allows us to backtrack when we reach the goal node
        * Find path taken by backtracking on each node's parent node
        * Check if path is optimal by comparing path costs
    * Each node can be represented using an object
* Keep track of nodes to explore next using a **frontier**
    * At the start of the search problem, the frontier contains just the initial state
    * If the frontier is empty, there is no solution
        * Empty frontier indicates no more states to explore, and since goal test has not been fufilled, no solution
    * Can be implemented using an object
        * Use attributes to keep track of nodes
        * Use methods to add/remove nodes
* Keep track of **explored states** 
    * Can be represented with a set

# Search algorithm

The basic structure of a search algorithm is as follows. With the data structures set up and the initial state in the frontier, run in a loop:

* If frontier is empty, no solution
* Else, remove node from frontier
    * Add state to set of explored states
    * Perform goal test on node. If node is goal state, solution found.
    * Else, expand node
        * Get all possible actions from node
        * Use transition state to get resultant nodes from these actions
        * If resultant node has not been explored, add to frontier

# Uninformed search algorithms

Two uninformed approaches to take for the search algorithm are **Breadth First Search** (BFS) and **Depth First Search** (DFS). They are uninformed search algorithms as they are strategies that don't use problem-specific knowledge to solve the problem.

Here, we assume that we keep track of states visited, otherwise DFS can get stuck in a loop.

## DFS

DFS will find a solution if:
* The solution exists
* The state space is finite, i.e. there are a finite number of states to explore

If the state space is infinite, the DFS algorithm may go down a path of infinite depth and thus never find the solution.

In summary, DFS is complete (assuming visited states are tracked) but not optimal

## BFS

BFS will find a solution if:
* The solution exists
* The branching factor is not infinite at any depth before the solution

If the BFS algorithm reaches a depth where a particular node has infinite branching factor, it will be stuck expanding that node and will not return a solution.

In addition: BFS will find an optimal solution if:
* The path cost function is non-decreasing
* Nodes on the same depth level have equal path cost

In summary, BFS is complete and optimal.

## BFS vs DFS

*b*: maximum branching factor of the search tree

*d*: depth of the least-cost solution

*m*: maximum depth of the state space

- | BFS | DFS
- | ----|----
**Time complexity** | 1+*b*+*b*<sup>2</sup>+*b*<sup>2</sup>+...+*b*<sup>d</sup> = *O*(*b*<sup>*d*</sup>) | *O*(*b*<sup>*m*</sup>)
**Space complexity** | *O*(*b*<sup>*d*</sup>) | *O*(*bm*)
**Complete** | Yes | Yes
**Optimal** | Yes | No

## BFS and DFS implementation

By implementing the frontier using different data structures, the search algorithm can be a Depth First or Breadth First Search. Two data structures suitable for implementing the frontier with are queues (FIFO) and stacks (LIFO).

Stack | Queue
------|---------
Depth First Search | Breadth First Search
Nodes added in last are removed first | Nodes Deepest nodes are expanded first | Shallowest nodes are expanded first

# Informed search algorithms

By using problem-specific knowledge, we can improve the performance of search algorithms. Two such informed search algorithms are [Greedy Best-First Search](https://www.youtube.com/watch?v=WbzNRTTrX0g&t=3269s) (GBFS) and [A* Search](https://www.youtube.com/watch?v=WbzNRTTrX0g&t=3915s) (prounounced A-star Search).

We make the same assumption as above that we keep track of states visited, otherwise like DFS, GBFS can get stuck in a loop.

## Evaluation function

These informed search algorithms use a evaluation function to decide what is the next step to take. One evaluation function is the previously mentioned path-cost function, *g(n)* which gives the cost from the initial node to the current node. 

Another evaluation function is the heuristic function *h(n)*. *h(n)* takes a state as an input and returns an estimate of how close the state is to the goal. 

We assume that the heuristic is admissible. Admissible means it never overestimates the true cost, i.e. it should never think the agent is further from the goal than it actually is. 

We also assume the heuristic is consistent. This means the heuristic value from a node to the goal shouldn't be more than the heuristic value of the node's child, plus the cost to make the step to the child. 

Mathematically, this means for any node where its heuristic value is given by *h(n)*, the heuristic value of it's child given by *h(n')*, and *c* being the cost to make that step, *h(n)* &ge; *h(n')* + *c*.

## Manhattan Distance

One specific type of heuristic is the Manhattan distance. If two nodes are represented using coordinates and the difference between the two nodes are represented using a vector, the Manhattan distance is the [1-norm](https://medium.com/@montjoile/l0-norm-l1-norm-l2-norm-l-infinity-norm-7a7d18a4f40c) of that vector.

The Manhattan Distance is only an estimate and not the actual distance to the goal as there are other factors, e.g. barriers in a maze.

## GBFS

Greedy Best-First Search's evaluation function *f(n)* based only on the heuristic function *h(n)*, i.e. *f(n)* = *h(n)*

Since GBFS is a greedy algorithm, it always chooses the locally optimum choice, i.e. the step with the lowest estimated distance to the goal, *h(n)*.

GBFS is complete (assuming we keep track of visited states) but not optimal.

## A* Search

A* Search uses an evaluation function of *f(n)* = *g(n)* + *h(n)*, i.e. it takes into account both past cost and predicted cost. 

When expanding nodes, it adds each child's path cost and heuristic value to rank which node to expand next. The node with the lowest *f(n)* is always expanded first.

Given the assumption that the heuristic function is admissible and consistent, A* Search is complete and optimal.

