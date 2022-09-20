# SymPy Physics Mechanics Proposal

Documentation and prototypes for the proposed refactoring of the `physics.mechanics` module of SymPy.

# Major considerations

While questions/considerations in the files themselves are labeled with `# QUESTION`. There are some major overall considerations listed below.

1. Should there be a `ModelObject`, which is inherited by all mechanical classes?

Pros:
- Useful for identification
- Could be used to share common properties and methods

Cons:
- 

2. The new file structure

3. Do we want a separate `Inertia` object, which inherits `DyaDic`?

4. `Constraint` is a `Matrix`

5. Should we model collisions? If so, how?
