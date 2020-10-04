from array import *
import itertools
data = itertools.combinations_with_replacement([1,2,3,4,5], 3)
for i in data:
    print(i)