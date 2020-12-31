# Chapter 14: Probabilistic Reasoning

**Baesyan Networks** as a DAG: nodes are random variables, arcs represent cause/effect (dipendence)

if youo constrain each node to have maximum k parents, storing the network requires n\*2^k space.

BN ⇔ P(X1, ..., XN) = Π_i P(Xi|parents(Xi))
= Π_i P(Xi|X1,...,Xi-1) # assuming Xi in topoligical order

---

Markov Blanket := parents + children + children’s parents
if you know the Markov Blanket of a node, that node is indipendent from other nodes

Local Semantics := parents
Local Semantics states that if you know the parents of a node, that node is indipendent from hin non-children/non-descendants

---

**Building the Baesyan Network**

    arcs = []
    for each randVar Xi:
        add Xi to BN
        parents =  min {parents: P(Xi|parents(Xi)) = P(Xi|X1, .., Xi-1)}
        arcs += [[p, Xi] for p in parents]

---

**Inference by Enumeraion**

P(X|e) = αP(X, e) = α \* sum_y P(X, e, y)

but requires O(n) space, O(2^n) time (repeated computations)

**Inference by Variable Elimination**

improve enumeration by avoiding repetitions: carry out summations right-to-left (i.e., bottom-up in the tree) & store intermediate results (factors) to avoid recomputation

P(B|j, m) = α \* f*B(B) \* f*\[(EA)^C JM](B)

... not sure how concatenation in fn work...

---

Inference is an NP-hard problem
