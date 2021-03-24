import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import powerset
import pickle

answer = frozenset(powerset({1,2}))
print(answer)
with open('output', 'wb') as f:
  pickle.dump(answer, f)
