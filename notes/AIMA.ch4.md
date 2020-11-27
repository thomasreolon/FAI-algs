# Chapter 4: Local Search

idea: use single current state to move to neighbours

---

###### _Algorithms_

**Greedy Local Search** Hill-Climbing

    0. actual_node = random_node
    1. get_neighbour with best score
    2. (neighbour.score > actual_node.score) ? actual_node = neighbour : return actual_node ;
    3. goTo 1.

incomplete: get stuck on local optima
variations: get_neighbour based on probability ; random-restart

**Simulated Annealing**
can also choose neighbours that do not improve the score

    0. t=0
    1. t += 1
    2. get random_neighbour
    3. E = neighbour.score - actual_node.score
    4. ( rand() < exp(E/t) ) ? actual_node = neighbour;
    5. goTo 1.

**Local Beam**
keep track of k states instead of 1. Usually every state ends up at the same hill.

    0. K = {k random states}
    1. neig = {}
    2. for k in K:
          neig.union(neighbours(k))
    3. K = best_k_from(neig)
    4. goTo 1.

**Genetic Algorithms**
successors states generated by combining two parent states.

    0. K = {k random states}
    1. children = {}
    2. for k1 in K:
          for k2 in K:
              children.add(new child(k1,k2))
    3. K = k_most_fit_from(children)
    4. goTo 1.

---

###### _Continuous Spaces_

**The Newton/Raphson Method**

    f := function with parameters X

    update parameters of f
    x = x - (Hessian^(-1)) (X) (grad(f))

---

###### _Non Deterministic Actions_

**AND-OR Search**
Problem as a tree.
Nodes on even levels -> OR nodes
Nodes on odd levels -> AND nodes
Every child of an AND node must be solvable.

    def solveORnode(node):
        if (is_goal(node)): return []
        for action, c in children(node):
            solution = solveANDnode(c)
            if (solution): return solution.push(a)
        return None

    def solveANDnode(node):
        solutions = {}
        for c in children(node):
            solution = solveORnode(c)
            if (not solution): return None
            solutions[c] = solution
        return [solutions]

    1. solveORnode(initialState)

---

###### _No/Partial Observations_

if no observations: states correspond to sets of possible environments.
Initial state = {every possible environment}

.

if partial observations: states correspond to a map (partialObservation -> setOfPossibleEnvironments)
InitialState = {
obs1: {every possible environment that respect obs1},
obs2: {every possible environment that respect obs2},
...
}

---

###### Online Search

**LRTA\***
heuristic updated during execution.

    g(s,s') := (s')? cost_from_to(s,s') + H(s') : h(s)

    1. next_state = neighbour_with_best_g
    2. if (H[next_state==null]):  H[next_state] = h(next_state)
    3. H[actual_state] = g_of(neighbour_with_best_g)
    4. actual_state = next_state
    5. goTo 1.