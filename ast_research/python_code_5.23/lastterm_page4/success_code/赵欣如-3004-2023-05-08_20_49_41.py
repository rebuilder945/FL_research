import math
def sushu(n):
    if n>=2 and type(n)==int:
        for i in range (2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
ls1=eval(input())
ls2=[]
for i in ls1:
    if sushu(i):
        ls2.append(i)
print(ls2)
