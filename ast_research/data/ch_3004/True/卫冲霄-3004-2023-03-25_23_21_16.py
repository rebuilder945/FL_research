import math
def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
    else:
        return False
ls=eval(input())
ls1=[]
for n in ls:
    if sushu(n):
        ls1.append(n)
print(ls1)
