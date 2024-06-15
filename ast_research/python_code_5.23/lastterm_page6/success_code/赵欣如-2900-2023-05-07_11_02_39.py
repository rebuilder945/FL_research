import math
def sushu(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
def huiwen(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=eval(input())
if n>1 and type(n)==type(1):
    for i in range(2,n):
        if sushu(i) and huiwen(i):
            print(i,end=" ")
else:
    print('illegal input')
