import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import transitiveclosure
import pickle

answer = frozenset(transitiveclosure(frozenset({(5,6), (6,7)})))
print(answer)
with open('output', 'wb') as f:
  pickle.dump(answer, f)
