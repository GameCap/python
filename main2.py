from array import *
import random
import itertools
array1=["АО", "ВС", "АС", "ВК", "ВО", "АТ", "СЕ", "ВХ", "АМ", "АВ", "АА", "АИ", "СА", "ВН", "ВЕ", "ВА", "СВ",
"ВМ", "АХ", "АЕ", "ВТ", "АР", "АН", "ВВ", "АК", "СН"]
array2=["0","1","2","3","4","5","6","7","8","9"]
array3=["E","T","I","O","P","A","H","K","X","C","B"]
data1 = itertools.combinations_with_replacement(array2, 4)
data2 = itertools.combinations_with_replacement(array3, 2)
t = list(''.join(i) for i in data1)
a = (random.choice(t))
y = list(''.join(b) for b in data2)
v = (random.choice(y))
print(random.choice(array1)+a+v)