import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import is_leapday

print(is_leapday("Feb 29, 2008 3:00:00pm"))
