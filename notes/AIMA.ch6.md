# Chapter 6: Constraint Satisfacitin Problems

    CSP problem := (X, D, C)

    X: {x1, ...}     "assignment of each varable, initially empty"
    D: {D1, ..., Dn} "domain of possible assignments for each variable ==> xi must belong to Di"
    C: "set of constraints"

    a solution is an complete assignment X that respect every constraint

Trying every possible assignment requires too much computation ( |possible_assignments| = productory_i[Di] ).

---

###### How to optimize

**Inferring: Propagating Constraints**
eg. AC-3 algorithm updates nearby domains inferring arc-consistency (forward checking)

propagating information from assigned to unassigned varables

    AC-3

    0. toCheck = every_arc_constraint
    1. arc = get_next(toCheck)
    2. if (size(D[arc[0]])==0): return false
    3. for x in D[arc[0]]:
           delete x if "unsatisfiable constraint x⇔y, y in D[arc[1]]"
    4. if (modified(D[arc[0]])):
          toCheck += [(adj, arc[0]) for adj in neighbours(arc[0])]
    5. if (size(toCheck)>0): toTo 1.
    6. return true

**Selecting Variable to Assign**
when choosing which variable to assign, give precedence to variables with the _smallest domain_ and variables with _more pending constraints_.

**Value Selection**
choose the value that _rules out the fewest choices_ for the
neighboring variables

**Backtracking Search**
if Partial Assignment becomes impossible, backtrack to a possible partial assignment.

IMPROVE: Conflict-Driven Backjumping
_find the choices that made the domain empty and backtrack to the latest one that was chosen with a heuristic._

    0. conflict_set =  keep track of which assignments reduced each domain
    1. nogood = conflict_set[node_with_empty_domain]
    2. tmp = "latest assignment in nogood"
    3. if (tmp=="forced choice"):
           nogood.remove(tmp)
           nogood.add(conflict_set[tmp])
           goTo 1.
    4. backtrack to tmp
    5. exclude actual tmp value from domain
    6. cheage assignment of tmp

IMPROVE: store noogods as additional constraints (don't try assignments that contain that pattern)

**Partitioniing**
check if the problem is decomposable in 2 indipendent parts. Divide et impera.

---

### solving CSP with local search

    state := complete assignment
    neighbours(state) := state with one assignment changed

    0. s = random_state
    1. s = neighbour(s) with least conflicts

---

Real problems involving CSP:

- task assignment
- scheduling

NOTE:
if no unary constraints ⇒ renaming domain is possible
eg. if X is a 3-coloring solution of a graph, you can swap colors obtaining valid solutions (A=red, B=blue ⇒ A=blue, B=red)

---

if the contraints generate a tree: easy

    0. n = random_node
    1. assign(n=??)
    2. forward checking (inference)
    3. if error: backtrack
    4. n = neighbour(n)
    5. goTo 1.

if nearly tree:

    if exist (x : x node in G && G -x is a tree ):
        for val in D[x]:
            res = solve(G, X={x=val})
            if (res != None): return res
