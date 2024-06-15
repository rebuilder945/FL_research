import math
def sushu(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def huiwenshu(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False

n=eval(input())
if n>0 and type(n)=type(1):
    for i in range(2,n+1):
        if sushu(1) and huiwenshu(i):
            print(i,end="")
else:
    print("illegal input")
    
