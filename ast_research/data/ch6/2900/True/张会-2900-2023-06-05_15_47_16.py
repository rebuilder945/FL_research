import math
def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                return False
        return True
def huiwenshu(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False

n=eval(input())
ls=[]
if n<=1 or n!=int(n):
    print('illegal input')
else:
    for i in range(2,n):
        if sushu(i) and huiwenshu(i):
            print(i,end=' ')

