import math
def sushu(n):
    for j in range(2,int(math.sqrt(n))+1):
        if n%j==0:
            return False
    return True
ls=eval(input())
s=[]
for i in ls:
    if sushu(i):
        s.append(i)
print(s)
