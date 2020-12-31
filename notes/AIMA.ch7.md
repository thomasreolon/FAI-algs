# Chapter 7: Logical Agents

    F = propositional logic formula
    eg. F = A∧not(C) || B∧C -> C
    (where [A,B,C] are literals  and [∧,not(), ||, ->] are respectively the logical operators [AND, NOT, OR, IMPLIES])

    problem: find an assignment (model) for A,B,C so that F is true

Finding a model (solvability problem) is NP-complete. Luckyly there is a process that optimize the search:

    1. F = CNF(F)
    2. model = SATsolver(F)

CNF := conjunction of disjunctions of literals (eg. (A v B) ∧ (not(B) v C))

a fast algorithm to obtain CNF(F) is Tseitin’s conversion

    0. F = formula; letter=0; conjunctions=[]
    1. AoperatorB = F.regex.find((literal, operator, literal), with operator in {∨, ∧, ⇔})
    2. conjunctions.push(CNF(letter ⇔ AoperatorB)) //can be precomputed
    3. F.substitute(AoperatorB, letter)
    4. letter++
    5. if (F is litteral): conjunction.push(F)
       else: goTo 1.
    6. return conjunctions

given some knowledge KB we want to prove that KB derives a formula (KB |= a). This equal to demonstrate that not(not(KB) || a) is unsatisfiable. So we can ask a SAT solver to solve **KB ∧ not(a)**, if there is no solution KB |= a.

methods to improve resolution of solvability:

- unit resolution: A ∧ B ∧ (not(B) v D) |= A ∧ B ∧ D
- unit propagation: A ∧ B ∧ (B v D) |= A ∧ B

old state of the art: get a formula in CNF, at each step assign one atom, giving priority to deterministic choices

**DPLL**

    1. if pure(only positive or negative) symbols exist, assign them
    2. if unit clauses exist, assign them
    3. S = get a random symbol
    4. assign S=true, if later fails, try S=false
    5. goTo 1.

improvement: conflic-driven backjumping

    0. confl = set()
    1. start = origianal disjuntion of the empty clause
    2. start = [*disjunc_where_decided[x] for x in start]
    3. while (size(start)>0):
            s = start.pop()
            if s was deterministic assignment:
                start.append(disjunction that made s deterministic)
            elif s was choice:
                confl.add(s)
    4. learn.append(conlf)
    5. bactrack to to most recent x in confl

Horn formulas: easy case --> solve unit clause; ramaining all false.

---

### KB agents

must be able to represent states/actions; have to be able to solve KB |= a.
3 main functions to interact with a KB:

- makePerceptSentence: Tells the KB the current percept
- makeActionQuery: Asks the KB for the next action
- makeActionSentence: Tells the KB that he has taken that action
