"""
# QUESTION
Constraints are in the end just a list of expression that should be zero.
Currently we represent them as being a Matrix with one column. With inheritance
we can make sure that these API friendly constraints are in the end just the
same, only now with a user-friendly interface.

+ - * methods, will give rather strange results, when inheriting Matrix.
"""
from sympy.core.backend import Matrix


class Constraint(Matrix):
    raise NotImplementedError


class _ConstraintComposition(Constraint):  # QUESTION not sure if this class is necessary
    raise NotImplementedError
