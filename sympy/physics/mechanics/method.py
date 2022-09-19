from abc import ABC, abstractmethod


class _Method(ABC):
    """Abstract Base Class for all methods.

    # QUESTION should we already implement these properties or leave them as
    abstractmethods? Implementation would save boiler plate and if a method
    would save it under a different attribute internally, one can overwrite the
    property.
    """

    @property
    def q(self):
        return self._q

    @property
    def u(self):
        return self._u

    @property
    def bodies(self):
        return self._bodies

    @property
    def loads(self):
        return self._loads

    @abstractmethod
    def mass_matrix(self):
        pass

    @abstractmethod
    def forcing(self):
        pass

    @abstractmethod
    def mass_matrix_full(self):
        pass

    @abstractmethod
    def forcing_full(self):
        pass

    @abstractmethod
    def _form_eoms(self):
        pass
