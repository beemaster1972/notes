from view.viewer import *
from service import *

class Controller:

    def __init__(self):
        self.viewer = Viewer()

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        pass
