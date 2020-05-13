# Week 0: Search

A search problem is one where given an environment that an agent is in, we would like the agent to be able to somehow look for a solution to that problem. A search problem comes in many forms, common examples include:

* 15 puzzle with sliding tiles
* Tic-tac-toe
* Maze
* Getting directions in Google Maps

## Terminology

* **Agent**: An agent is an entity that perceives its environment and acts on that environment in some way.
* **State**: A state is some configuration of the agent in its environment.
    * Initial state: State where the agent begins in the problem/algorithm
* **Actions**: Choices available in any given state
* **Path cost**: Cost of any action taken 

## Implementation

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

## Search Algorithm

With the data structures set up and the initial state in the frontier, run in a loop:

* If frontier is empty, no solution
* Else, remove node from frontier
    * Add state to set of explored states
    * Perform goal test on node. If node is goal state, solution found.
    * Else, expand node
        * Get all possible actions from node
        * Use transition state to get resultant nodes from these actions
        * If resultant node has not been explored, add to frontier

## Uninformed search algorithms

Two uninformed approaches to take for the search algorithm are **Breadth First Search** (BFS) and **Depth First Search** (DFS). They are uninformed search algorithms as they are strategies that don't use problem-specific knowledge to solve the problem.

## DFS

DFS will find a solution if:
* The solution exists
* The state space is finite, i.e. there are a finite number of states to explore

If the state space is infinite, the DFS algorithm may go down a path of infinite depth and thus never find the solution.

## BFS

BFS will find a solution if:
* The solution exists
* The branching factor is not infinite at any depth before the solution

If the BFS algorithm reaches a depth where a particular node has infinite branching factor, it will be stuck expanding that node and will not return a solution.

In addition: BFS will find an optimal solution if:
* The path cost function is non-decreasing
* Nodes on the same depth level have equal path cost

## BFS and DFS implementation

By implementing the frontier using different data structures, the search algorithm can be a Depth First or Breadth First Search. Two data structures suitable for implementing the frontier with are queues (FIFO) and stacks (LIFO).

Stack | Frontier
------|---------
Depth First Search | Breadth First Search
Nodes added in last are removed first | Nodes Deepest nodes are expanded first | Shallowest nodes are expanded first

