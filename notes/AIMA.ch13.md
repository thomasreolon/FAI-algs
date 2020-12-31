# Chapter 13: Uncertainity

non deterministic actions / partial obsevability ==> use of probability

Maximum expected utility --> probability utility

**properties of probability**
P(a ∧ b) = P(a|b) · P(b)
P(X, Y) = P(X|Y) · P(Y)
P(X1, ..., Xn) = Π\*i P(Xi|X1, ..., Xi−1)
P(cause|effect) = P(effect|cause)P(cause)/P(effect) ---- _bayes rule_

**Diagnosis**
α = 1/P(Effect1, ..., Effectn)
P(Cause|Effect1, ..., Effectn) = α \* P(Cause) \* Π_i P(Effect_i|Cause)

## Example of Computation

evidence = not pit ((1,1), (1,2), (2,1)) ; not breeze((1,1)) ; breeze((1,2),(2,1))

evidence = b*, p*

P(query/evidence) = α*P(query, evidence) = α\*sum_u\*P(query, evidence, u) = ...
... = α\*P(p*)\*P(query)\*sum_fringe[ P(b*|p*,query,fringe) \* P(fringe)]

**TL;DR: average through uncertainity than simplify (indipenences)**
