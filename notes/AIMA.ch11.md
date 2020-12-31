# Chapter 11: Planning Applications

We add RESOURCES to the problem of planning (consume, use)

![plan](images/egplan.JPG)

##### Scheduling without considering RESOURCES

    1. dependencies_graph = solve_planning_problem()
    2. ES[initial state] = 0
    3. for state in order_topological(plan):
           ES[state] = max( [ES[prev]+duration(prev)   for prev in actions_before(state)] )
    4. LS[goal state] = ES[goal state]
    5. for state in order_topological(plan, reverse=True):
           LS[state] = max( [LS[succ]-duration(succ)   for succ in actions_after(state)] )

Example of a scheduling

![sched](images/egScheduling.JPG)

##### Hierarchical Planning

mmmm: like a DFS of possible actions, if goal is reached: return plan

##### Planning & non-determinism

3 types: Sensorless planning, Conditional planning, Execution monitoring and replanning

Different from search for the representations: belief state is a logic formula; actions have preconditions and effect that modify the state
