# Problem: 	Assign a color to each state of the graph G.
#           You cannot assign the same color to neighboring states.
#           You can use only {'red', 'blue', 'green'}.
import random

# Formalizing the problem of coloring


class CSPColorStates():
    def __init__(self, G, colors: set):
        self.X = {}       # assignments: empty at beginning
        # domains: possible colors for each state
        self.D = {x: {*colors} for x in G.keys()}

        # constraints:  if (j in G[i]):  X[i] != X[j]
        # if edge (i,j) exists in the graph: check arc_constraint(node_i.color != node_j.color)
        self.G = G


######################################## INPUT ##########################################################
G = {
    0: {1, 2},
    3: {1, 2, 4},
    1: {0, 2, 3},
    2: {0, 1, 3, 4, 5},
    4: {3, 2, 5},
    5: {2, 4},
    6: {},
}


csp = CSPColorStates(G, {'red', 'blue', 'green'})
f = 1       # just for the prints


######################################## SOLUTION ##########################################################

# solve: takes a 3coloringCSP problem and solves it: ((until solution found){color best node, infer})
# ac3:   support function used by solve function that does the inferring step

# receives a tuple containing the new assignemt (state <-- color)
# infer what the neighbours can contain after the assignment
# returns a dict that map:  states --> colors to remove from their domain
def ac3(last_assignment: tuple, csp: CSPColorStates):
    result = {x: set() for x in csp.G.keys()}
    to_check = [last_assignment]     # updated node
    visited = set(csp.X.keys())

    while(len(to_check) > 0):
        node, color = to_check.pop()
        visited.add(node)

        # update neighbours of the node
        for adj in csp.G[node]:
            # exclude already assigned nodes && consider only new colors
            if adj not in visited and color in csp.D[adj] and color not in result[adj]:
                # we'll have to subtract this color from D[adj]
                result[adj].add(color)

                options, to_esclude = csp.D[adj], result[adj]
                if (len(options) == len(to_esclude)):
                    # this means that the neighbour can't have any new colors: not a valid solution
                    return None
                elif (len(options) == len(to_esclude)+1):
                    # this means that the neighbour can have only one possible color
                    to_check.append((adj, tuple(options-to_esclude)[0]))

    return result


def solve(csp: CSPColorStates):
    global f
    # get useful variables
    X, D, G = csp.X, csp.D, csp.G
    n_states = len(G.keys())

    # check if i have a full assignment
    if (len(X) == n_states):
        # stop computation: self.X now contains a valid solution
        return True

    # i have a partial assignment:
    # non_assigned_states = all_states    -   assigned_states
    non_assigned_states = list(set(csp.G.keys()).difference(csp.X.keys()))
    # before: states with smaller domain
    non_assigned_states.sort(key=lambda state: -len(D[state]))

    # for each state/color combination (until a valid solution is found):
    for state in non_assigned_states:
        solved = False
        for color in D[state]:
            inference = ac3((state, color), csp)
            print(f"{'-'*f}> assign {color} to {state}? {bool(inference)}")
            if (inference):
                f += 1
                X[state] = color   # assign color to state
                csp.D = {x: D[x]-inference[x]
                         for x in D.keys()}  # update Domains
                solved = solve(csp)
                if (solved):
                    break

                # if not solved: Backtrack
                f -= 1
                del X[state]
                csp.D = {x: D[x].union(inference[x]) for x in D.keys()}
        if (solved):
            break

    return solved


valid = solve(csp)

print(
    f"\033[96massignment:\n{(valid and csp.X) or 'no solution was found'}\033[0m"
)
