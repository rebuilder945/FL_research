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
if n<2 or type(n)!=type(1):
    print("illegal input")
else:
    for i in range(1,n):
        if sushu(n) and huiwenshu(n):
            print(i,end="")
    
