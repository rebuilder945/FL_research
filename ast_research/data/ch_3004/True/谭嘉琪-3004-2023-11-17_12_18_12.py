import math
ls=eval(input())
ls1=[]
def sushu(n):
    for i in range(2,int(math.sqrt(n)+1)):
        b=n%i
        if b==0:
            break
    else:
        ls1.append(n)
for n in ls:
    if n>1:
        sushu(n)
print(ls1)
