import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import evalsum

x = 1+1.2-4.34343434000
print(x)
print(evalsum("1+1.2-4.34343434000"))
