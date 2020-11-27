# Chapter 8: First Order Logic

FOL basic elements:

**Constants**: KingJohn, 2, UCB, ... (are objects)
**Predicates**: Brother, >, ... (returns bools)
**Functions**: Sqrt, Lef tLegOf, ... (returns objects)
**Variables**: x, y, a, b, ...
**Connectives**: ∧ ∨ ¬ ⇒ ⇔
**Equality**: =
**Quantifiers**: ∀ ∃

terms = constants + predicates + variables (identify objects)
atomic sentence = predicates + equality
complex sentence = sentences joined by connectives

examples:

    everyone likes icecream  -> ∀x.Like(x, icecream)
    if x<y and y<z than x<z  -> ∀x,y,z.((x<y ∧ y<z) ⇒ x<z)
    if you love every animal, someone will love you -> ∀p.[∀a.(Animal(a) ∧ Love(p,a)) ⇒ ∃x.(Love(x,p))]

Knowlodge engineering:

- delineate task/question that the KB must support
- gather expert knowledge
- decide vocabolary (ontology)
- encode general knowlwdge
- use: give info about a problem
- use: make queries
- debug?
