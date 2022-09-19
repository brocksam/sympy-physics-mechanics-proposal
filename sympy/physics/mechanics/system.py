from .method import _Method
from .kane import KanesMethod
from .loads import _Load, _LoadComposition


# QUESTION should in the end be compatible to for example pydy
# QUESTION what is the best name: JointsMethod, Model or System
class System(_Method):
    def add_coordinates(self, coordinates, ifexists='raise'):
        pass

    def add_speeds(self, speeds, ifexists='raise'):
        pass

    def add_kdes(self, kdes):
        pass

    def add_joints(self, joints, ifexists='raise'):
        pass

    def add_bodies(self, bodies, ifexists='raise'):
        pass

    def add_loads(self, loads, ifexists='raise'):
        if isinstance(loads, _LoadComposition):
            pass
        elif isinstance(loads, _Load):
            pass

    def apply_force(self, point, force):
        pass

    def _form_eoms(self, method=KanesMethod):
        pass

    @property
    def mass_matrix(self):
        pass

    @property
    def mass_matrix_full(self):
        pass

    @property
    def forcing(self):
        pass

    @property
    def forcing_full(self):
        pass
