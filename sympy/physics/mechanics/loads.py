"""
# QUESTION
Using separate objects for loads is easier to recognize than a tuple, as is
currently used. However how should one go about using for example an actuator,
e.g. spring. An actuator exerts multiple loads. An option would be to use a
_LoadComposition class, which internally has a list storing all _Load's. This
will however that you'll have to check whether your dealing with a load
composition or just with a single load, which may not be ideal.

An option would be to use __add__, which gives a load composition. And that
after gathering all loads in a single load composition, one can easily use this
in the further processing of all system loads. This will however result in quite
terrible typing.

# QUESTION force1 + force2 --> _LoadComposition?
    Yes --> _LoadComposition should not be protected
"""

from abc import ABC, abstractmethod
from sympy.physics.vector import Point, Vector
from .bodies import _Body


class _Load(ABC):
    """Abstract base class for the various loading types.

    """

    def __init__(self, location, vector):
        self._set_location(location)
        self._set_vector(vector)

    @property
    def vector(self):
        return self._vector

    @property
    def location(self):
        return self._location

    @abstractmethod
    def _set_location(self, location):
        pass

    @abstractmethod
    def _set_vector(self, vector):
        pass


class Force(_Load):
    point = _Load.location
    force = _Load.vector

    def __init__(self, point, force):
        super().__init__(point, force)

    def _set_location(self, point):
        if isinstance(point, _Body):
            self._location = point.masscenter
        elif isinstance(point, Point):
            self._location = point
        else:
            raise TypeError('Force location should of type Point.')

    def _set_vector(self, force):
        if isinstance(force, Vector):
            self._vector = force
        else:
            raise TypeError('Force vector should be of type Vector.')


class Torque(_Load):
    raise NotImplementedError


class Pressure(_Load):
    raise NotImplementedError


class _LoadComposition(_Load):
    raise NotImplementedError


class LinearSpring(_LoadComposition):  # QUESTION Linear?
    raise NotImplementedError


class LinearDamper(_LoadComposition):
    raise NotImplementedError


class SpringDamper(_LoadComposition):
    # QUESTION how to relate this to Spring and Damper
    raise NotImplementedError


class _Muscle(_LoadComposition):
    """Abstract base class for various muscle types.
    TODO Will be moved out of the mechanics module
    """
    raise NotImplementedError
