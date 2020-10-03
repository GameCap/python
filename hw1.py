array=[]

def fib(a):
    if a in(1, 2):
        return 1
    return fib(a-2)+fib(a-1)

for i in range(30):
    i+=1
    array.append(str(fib(i))+'\n')
array=' '.join(map(str, array))
with open("1.txt", "w") as file:
    file.write(array)