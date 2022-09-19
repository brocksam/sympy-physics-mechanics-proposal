from abc import ABC, abstractmethod

# QUESTION currently one cannot use a Particle with Joint(s) due to the missing
# frame argument
class _Body(ABC):
    @property
    @abstractmethod
    def mass(self):
        pass

    @property
    @abstractmethod
    def masscenter(self):
        pass

    # QUESTION If potential_energy is a property, shouldn't kinetic_energy be a
    # property as well?
    @property
    @abstractmethod
    def potential_energy(self):
        pass

    @abstractmethod
    def kinetic_energy(self, frame):
        pass

    @abstractmethod
    def linear_momentum(self, frame):
        pass

    @abstractmethod
    def angular_momentum(self, point, frame):
        pass

    @abstractmethod
    def parallel_axis(self, point, frame):
        pass


class Particle(_Body):
    raise NotImplementedError


class RigidBody(_Body):
    raise NotImplementedError


class SoftBody(_Body):
    raise NotImplementedError
