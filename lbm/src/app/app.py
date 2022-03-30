# Custom imports
from lbm.src.core.factory   import *
from lbm.src.app.cavity     import *
from lbm.src.app.turek      import *
from lbm.src.app.poiseuille import *
from lbm.src.app.array      import *
from lbm.src.app.step       import *
from lbm.src.app.stepVar    import *
from lbm.src.app.cylinder   import *

# Declare factory
app_factory = factory()

# Register apps
app_factory.register("cavity",     cavity)
app_factory.register("turek",      turek)
app_factory.register("poiseuille", poiseuille)
app_factory.register("array",      array)
app_factory.register("step",       step)
app_factory.register("stepVar",    stepVar)
app_factory.register("cylinder",   cylinder)
