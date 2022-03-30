# Generic imports
import os
import sys

# Custom imports
from lbm.src.app.app      import *
from lbm.src.core.lattice import *
from lbm.src.core.run     import *

########################
# Run lbm simulation
########################
if __name__ == '__main__':

    if len(sys.argv) == 2:
        app_name = 'stepVar'
        app = app_factory.create(app_name)
        
        app.create_obstacles(obs_1_size = 1.5, obs_2_size = 1.0)
        
        ltc = lattice(app)
        run(ltc, app)
    
    else:
        print('Unrecognized configuration, got the following arguments:')
        print(sys.argv)
        exit()
    




