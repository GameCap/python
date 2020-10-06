from array import *
import itertools
array=[1,2,3,4,5]
data = itertools.combinations_with_replacement(array, 3)
for i in data:
    print(i)
    
    
