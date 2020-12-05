#!/usr/bin/env python3
# See setup.sh
import sys, os
dist_package_index = sys.path.index('/usr/local/lib/python3.6/dist-packages')
sys.path = sys.path[:dist_package_index] + ['/usr/local/lib/python3.6/site-packages'] + sys.path[dist_package_index:]
exec(open('rapidsai-csp-utils/colab/update_modules.py').read(), globals())
