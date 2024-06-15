def sushu(x):
    for i in range(2,x//2+1):
        if x % i == 0:
            return 
    return x
n=eval(input())
a=[]
for x in n:
    if sushu(x):
        a.append(x)
for x in a:
    if x == 1:
        a.remove(x)
print(a)
