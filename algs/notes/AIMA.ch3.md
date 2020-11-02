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

Use a heuristic that suggests the possible cost for reaching the goal from a given state.

    def heuristic  h

    h:  (state) => cost

    - admissible <=>     h(n) <= h*(n)       with h* the true cost
    - consistent <=>     h(n) <= c(n,a,n') + h(n')

- Greedy Search
- A\* (optimal if h is admissible)
