import math
def sushu(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def huiwenshu(n):
    sn=str(n)
    if sn==sn.sort(reverse=True):
        return True
n = eval(input())
if math.floor(n)==n and n>0:
    for m in range(n):
        if sushu:
            if huiwenshu:
                print(m,end="")
else:
    print("illegal input")
