from abc import ABC, abstractmethod


class Joint(ABC):
    """Abstract base class for all specific joints.

    """
    def __init__(self, name, parent, child, coordinates=None, speeds=None,
                 parent_point=None, child_point=None, parent_interframe=None,
                 child_interframe=None):  # TODO Incomplete
        raise NotImplementedError

    @property
    def name(self):
        """Name of the joint."""
        return self._name

    @property
    def parent(self):
        """Parent body of Joint."""
        return self._parent

    @property
    def child(self):
        """Child body of Joint."""
        return self._child

    @property
    def coordinates(self):
        """Matrix of the joint's generalized coordinates."""
        return self._coordinates

    @property
    def speeds(self):
        """Matrix of the joint's generalized speeds."""
        return self._speeds

    @property
    def kdes(self):
        """Kinematical differential equations of the joint."""
        return self._kdes

    @property
    def parent_point(self):
        """Attachment point where the joint is fixed to the parent body."""
        return self._parent_point

    @property
    def child_point(self):
        """Attachment point where the joint is fixed to the child body."""
        return self._child_point

    @property
    def parent_interframe(self):
        return self._parent_interframe

    @property
    def child_interframe(self):
        return self._child_interframe

    @abstractmethod
    def _generate_coordinates(self, coordinates):
        """Generate Matrix of the joint's generalized coordinates."""
        pass

    @abstractmethod
    def _generate_speeds(self, speeds):
        """Generate Matrix of the joint's generalized speeds."""
        pass

    @abstractmethod
    def _orient_frames(self):
        """Orient frames as per the joint."""
        pass

    @abstractmethod
    def _set_angular_velocity(self):
        """Set angular velocity of the joint related frames."""
        pass

    @abstractmethod
    def _set_linear_velocity(self):
        """Set velocity of related points to the joint."""
        pass


class PinJoint(Joint):
    raise NotImplementedError


class PrismaticJoint(Joint):
    raise NotImplementedError


class CylindricalJoint(Joint):
    raise NotImplementedError


class PlanarJoint(Joint):
    raise NotImplementedError


class SphericalJoint(Joint):
    raise NotImplementedError
