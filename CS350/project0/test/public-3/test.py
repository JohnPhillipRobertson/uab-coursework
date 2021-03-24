import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import phonenumber

print(phonenumber('(123) 456-7890'))
