from array import *
import random
import itertools
array=["a","b","c","d","f"]
data = itertools.combinations_with_replacement(array, 3)
for i in data:
    print(''.join(i))
    
    
