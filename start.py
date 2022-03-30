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
    
    app_name = 'stepVar'
    app = app_factory.create(app_name)

    if len(sys.argv) == 3:
        app.create_obstacles(obs_1_size = float(sys.argv[1]), obs_2_size = float(sys.argv[2]))
        
    elif len(sys.argv) == 1:
        app.create_obstacles(obs_1_size = 1.5, obs_2_size = 1.0)

        
    else:
        print('Unrecognized configuration, use python3 start.py size1 size2.  I got the following arguments:')
        print(sys.argv)
        exit()
       
    ltc = lattice(app)
    run(ltc, app)
    

    




