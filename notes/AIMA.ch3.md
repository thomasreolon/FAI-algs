# Chapter 3: SEARCH ALGORITHMS

    def. Problem as a directed graph G = (V, E)

    V = {states}
    E = {actions}

    solution: path that connect the starting node to a goal node

Search happens inside the agent (simulation of the possible choices it can make).

### Uninformed Search

- BFS (drawbacks: exponential consumption of memory)
- DFS (drawbacks: risky in non finite graphs)
- UCS (weighted BFS)
- Iterative DFS

### Informed Search

Use a heuristic h(n) that estimates how close a state n is to a goal.

    def heuristic  h

    h:  (state) => cost

    - admissible ⇔     h(n) <= h*(n)       with h* the true cost
    - consistent ⇔     h(n) <= c(n,a,n') + h(n')

- Greedy Search
- A\* (optimal if h is admissible)

---

b: branching factor (average number of edges-1)
d: depth of the goal node
m: total deepness of graph

**BFS**
expand first the closest node to start (not already expanded). Uses a _queue_.

| time   | memory | complete | optimal |
| ------ | ------ | -------- | ------- |
| O(b^d) | O(b^d) | yes      | yes     |

**UCS**
expand first the node with the lowest path cost. (if edges have the same cost is like BFS). Uses a _priority queue_ (heap).

| time             | memory           | complete | optimal |
| ---------------- | ---------------- | -------- | ------- |
| O(b^"eff.depth") | O(b^"eff.depth") | yes      | yes     |

**DFS**
expand first the deepest node. Uses a _stack_.

| time   | memory | complete                   | optimal |
| ------ | ------ | -------------------------- | ------- |
| O(b^m) | O(bm)  | iff finite & prevent loops | no      |

**IDS**
expand first the deepest node. Uses a _stack_.

| time   | memory | complete | optimal |
| ------ | ------ | -------- | ------- |
| O(b^d) | O(bm)  | yes      | yes     |

**Bidirectinal Search**
start a search from end-node and start-node simultaneously.
Complexity: _b^(d/2) + b^(d/2)_ << _b^d_

---

**Greedy Search**
select node with lowest _h(n)_ in the frontier. Based on _priority queue_.

| time   | memory | complete | optimal |
| ------ | ------ | -------- | ------- |
| O(b^d) | O(b^d) | no       | no      |

**A\***
select node with lowest _c(n) + h(n)_ in the frontier, with c(n) being the real cost for getting to n from the start-node. Based on _priority queue_.

e: "relative error of h" < 1

| time      | memory | complete | optimal |
| --------- | ------ | -------- | ------- |
| O(b^(de)) | O(b^d) | yes      | yes     |

---

    DOMINANCE
    h1(n), h2(n)  are admissible heuristics
    h3(n) := max(h1(n), h2(n))         is a better heuristic

    RELAXED PROBLEMS
    find heuristic of the relaxed problem (if the definition of the problem is formal use a ABSolver)
