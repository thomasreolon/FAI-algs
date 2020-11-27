# Chapter 9: FOL Inference

tranformation that can be applied to a formula:

    multiple substitution:      e{a1/b1, a2/c2} --> sub({a2/b2},sub({a1/b1},e))
    equal term substitution:    A^(b=c) --> A^(b=c)^A{b/c}
    equal subformula substitution: A^(b1<->b2) --> A{b1/b2}^(b1<->b2)
    universal instantation:     ∀x.A --> ∀x.A ^ A{x/t}      (t: general term)
    existential instantiation:  ∃x.A --> A{x/c}             (c: new constant)

About Universal Instantiation:

- UI can be applied several times to add new sentences
- The new KB is **logically equivalent** to the old KB

About Existential Instantiation:

- EI can be applied once to replace the existential sentence
- The new KB is not equivalent to the old,
  but is (un)satisfiable iff the old KB is (un)satisfiable
  ⇒ **the new KB can infer β iff the old KB can infer β**

---

- **Forward Chaining**: unify conjuctions to create the formla we want to prove.
  It is sound (solutions found are correct), and complete.

          1. for each formula like (p1^...^pn ⇒ q) in KB:
          2.     find a conjunction of formulas of the KB that  can be unified with p1^...^pn
          3.     omega = subsitution that unifies p1...pn with point 2.
          4.     if sub(q, omega) == thing_to_prove:
                      return true
                 else:
                      KB.add(sub(q, omega))
          5. if something was added to KB: goTo 1.
          6. return false



          eg.
          KB = {
              cat(meo) ; has(Luca, meo) ;
              ∀x,y.(cat(x) ^ has(y, x) ⇒ ¬∃z.(has(y, z) ^ mouse(z)))
          }
          thing_to_prove = "Luca doesn't have a mouse"

          1. formula = cat(x) ^ has(y, x) ⇒ ¬∃z.(has(y, z) ^ mouse(z))
          2. p'1 = cat(meo), p'2=has(Luca, meo)
          3. omega = {x/meo, y/Luca}
          4. ...

- **Backward Chaining**: inefficient. goal as a set of conjuctions. substitute a conjunction C of the goal with a set of conjunctions C' if (C'⇒Q is in the KB && are_unifiable(Q, C)).

- **FOL to CNF**: fast & complete. Transform to PL & prove that KB |= a showing that KB ^ not(a) is unsatisfiable

        # simplify KB
        1. simplify implications and biconditionals
        2. push inward negations
        3. unique variable names
        4. skolemize
        5. drop universal
        6. CNF-ization

        # algorithm to prove goal
        1. remaining = not(goal)
        2. p1...pi...pn = disjunction in KB
        3. if unifiable(pi, part_of_remaining):
               goal = (pi..pn + remaining){unify(pi, part_of_remaining)} - pi
        4. if remaining != {}: goTo 1.
        5. return true
