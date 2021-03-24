import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import cartesianproduct

print(frozenset(cartesianproduct([{1},{2},{3,4,5}])))
print(frozenset({(1,2,3),(1,2,4),(1,2,5)}))
