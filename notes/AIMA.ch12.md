# Knowledge Representation

- knowledge engineering: how to represent the world
- ontological engineering: how to build general-purpose ontologies

**categories**
subcategory & objects ineriths properties. KR organizes objects into categories.

- composed classes: PartOf(a, b) ## reflexive and transitive
- natural kinds: typical(a) ## x in typical(tomato) --> red(x)
- measures: Length(L1) = Inches(1.2) ## orderable (can have no scale eg. beauty)

- countable objects VS stuff

**situational calculus**
initial state s := situation
result(s, a) := situation && result is injective

Φ := preconditions ## eg. (Alive(Agent, s) ∧ Have(Agent, Arrow, s)) → Poss(Shoot, s)

**intervals**

- T(f,t) # if fluent f is True at time t
- Happens(e,i) # if event e happens over the time interval i
- Initiates(e,f,t) # if event e causes fleuent f to start at time t
- Clipped(f,i) # if fluent f become false during interval i
- Restored(f, i) # if fluent f is sometimes true during i
- ....
- Time(m) # moment m --> seconds
- Begin(i), End(i) # return moments of interval
- Duration(i) # return the seconds of the interval

reification: AT(Luca, Belluno) -> T(AT(Luca,Belluno), time)

_Allen's interval algebra_

- Meet(i,j)
- Before(i,j)
- After(i,j)
- During(i,j)
- Overlap(i,j)
- Starts(i,j)
- Finishes(i,j)
- Equals(i,j)

Need for referential opacity with multiple agents. -> K_A(B) := A knows B

w0 --K_a-> w1 := w1 is accessible with K_a from w0 (stuff in w0 are consistent with w1)

#### Categories

- Semantic Networks
- Description Logics

**Semantic Networks**

nodes: concepts (categories/individuals)
edges: binary relations (isA, instanceOf)

n-ary relations: from event node one edge for each type of relation
networks have limitation: no disjunctions, no negations, ...

**Description Logics**

T-boxes: define categories
A-boxes: instance objects/relations

Used to design ontologies or make query on it
