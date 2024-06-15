import math
def sushu(n):
    for j in range(2,n//2+1):
        if n%j==0:
            return False
    return True
ls=eval(input())
s=[]
for i in ls:
    if i>1 and sushu(i):
        s.append(i)
print(s)
