# Week 3: Optimization <!-- omit in toc -->

- [Local search](#local-search)
  - [State-space landscape](#state-space-landscape)
  - [Hill-climbing](#hill-climbing)
    - [Variants](#variants)
  - [Simulated annealing](#simulated-annealing)
- [Linear Programming](#linear-programming)
  - [Algorithms](#algorithms)
- [Constraint satisfaction](#constraint-satisfaction)
  - [Definitions](#definitions)
  - [Arc consistency algorithms](#arc-consistency-algorithms)
  - [CSPs as Search Problems](#csps-as-search-problems)
  - [Backtracking search](#backtracking-search)
    - [Backtracking search with arc consistency](#backtracking-search-with-arc-consistency)
    - [Selecting unassigned variable](#selecting-unassigned-variable)
    - [Selecting value in domain](#selecting-value-in-domain)

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

Basic hill-climbing algorithm only gives local maxima/minima, so variants exist to solve the problem.

### Variants

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

# Linear Programming

* Minimize a cost function <code>c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> + ... + c<sub>n</sub>x<sub>n</sub></code>
* With constraints of form <code>a<sub>1</sub>x<sub>1</sub> + a<sub>2</sub>x<sub>2</sub> + ... + a<sub>n</sub>x<sub>n</sub> ≤ b</code> or of the form <code>a<sub>1</sub>x<sub>1</sub> + a<sub>2</sub>x<sub>2</sub> + ... + a<sub>n</sub>x<sub>n</sub> = b</code>
* With bounds for each variable <code>l<sub>i</sub> ≤ x<sub>i</sub> ≤ u<sub>i</sub></code>

## Algorithms

* Simplex
* Interior-Point

# Constraint satisfaction

* Set of variables <code>{X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>n</sub>}</code>
* Set of domains for each variable <code>{D<sub>1</sub>, D<sub>2</sub>, ..., D<sub>n</sub>}</code>
* Set of constraints `C`

## Definitions

| Term              | Definition                                                                                                                                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hard constraints  | Constraints that must be satisfied in a correct solution                                                                                                                                                                           |
| Soft constraints  | Constraints that express some notion of which solutions are preferred over others                                                                                                                                                  |
| Unary constraint  | Constraint involving only one variable                                                                                                                                                                                             |
| Binary constraint | Constraint involving two variables                                                                                                                                                                                                 |
| Node consistency  | When all the values in a variable's domain satisfy the variable's unary constraints                                                                                                                                                |
| Arc consistency   | When all the values in a variable's domain satisfy the variable's binary constraints, i.e. to make `X` arc-consistent with respect to `Y`, remove elements from `X`\'s domain until every choice for X has a possible choice for Y |

## Arc consistency algorithms

For two nodes:
<pre><code>function REVISE(<em>csp</em>, X, Y):
  <em>revised</em> = <em>false</em>
  for <em>x</em> in <em>X.domain</em>:
    if no <em>y</em> in <em>Y.domain</em> satisfies constraint for (<em>X</em>, <em>Y</em>):
      delete <em>x</em> from <em>X.domain</em>
      <em>revised</em> = <em>true</em>
  return <em>revised</em></code></pre>

For ensuring arc consistency for all nodes:
<pre><code>function AC-3(<em>csp</em>):
  <em>queue</em> = all arcs in <em>csp</em>
  while <em>queue</em> non-empty:
  (<em>X</em>, <em>Y</em>) = DEQUEUE(<em>queue</em>)
  if REVISE(<em>csp</em>, X, Y):
    if size of <em>X.domain</em> == 0:
      return false
    for each <em>Z</em> in <em>X.neighbours</em> - {<em>Y</em>}:
      ENQUEUE(queue, (<em>Z</em>, <em>X</em>))
  return <em>true</em></code></pre>

## CSPs as Search Problems

* Initial state: empty assignment (no variables)
* Actions: add a {variable = value} to assignment
* Transition model: shows how adding an assignment changes the assignment
* Goal test: check if all variables assigned and constraints all satisfied
* Path cost function: all paths have same cost

## Backtracking search

<pre><code>function BACKTRACK(<i>assignment</i>, <i>csp</i>):
  if <i>assignment</i> complete:
    return <i>assignment</i>
  <i>var</i> = SELECT-UNASSIGNED-VAR(<i>assignment</i>, <i>csp</i>)
  for <i>value</i> in DOMAIN-VALUES(<i>var</i>, <i>assignment</i>, <i>csp</i>):
    if <i>value</i> consistent with <i>assignment</i>:
      add {<i>var</i> = <i>value</i>} to <i>assignment</i>
      <i>result</i> = BACKTRACK(<i>assignment</i>, <i>csp</i>)
      if <i>result</i> not failure:
        return <i>result</i>
    remove {<i>var</i> = <i>value</i>} from <i>assignment</i>
  return <i>failure</i></code></pre>

By interleaving maintaining arc consistency with the backtracking search algorithm, we can increase the efficiency of the search.

### Backtracking search with arc consistency

<pre><code>function BACKTRACK(<i>assignment</i>, <i>csp</i>):
  if <i>assignment</i> complete:
    return <i>assignment</i>
  <i>var</i> = SELECT-UNASSIGNED-VAR(<i>assignment</i>, <i>csp</i>)
  for <i>value</i> in DOMAIN-VALUES(<i>var</i>, <i>assignment</i>, <i>csp</i>):
    if <i>value</i> consistent with <i>assignment</i>:
      add {<i>var</i> = <i>value</i>} to <i>assignment</i>
      <i>inferences</i> = INFERENCE(<i>assignment</i>, <i>csp</i>)
      if <i>inferences</i> not failure:
        add <i>inferences</i> to <i>assignment</i>
      <i>result</i> = BACKTRACK(<i>assignment</i>, <i>csp</i>)
      if <i>result</i> not failure:
        return <i>result</i>
    remove {<i>var</i> = <i>value</i>} and <i>inferences</i> from <i>assignment</i>
  return <i>failure</i></code></pre>

### Selecting unassigned variable

We can use heuristics to better determine which variable to assign a value to next.

* Minimum remaining values (MRV) heuristic: select the variable that hs the smallest domain
* Degree heuristic: select the variable that has the highest degree

### Selecting value in domain

* Least-constraining values heuristic: return variables in order by number of choices that are ruled out for neighbouring variables
  * Try least-contraining values first