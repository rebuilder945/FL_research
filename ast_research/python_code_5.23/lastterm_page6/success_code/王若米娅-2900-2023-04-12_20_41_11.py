
def sushu(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return False
        else:
            return True
def huiwenshu(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False

n=eval(input())
if n>1 and type(n)==type(1):
    for x in range(2,n):
        if sushu(x) and huiwenshu(x):
            print(x,end=' ')
else:
    print("illegal input")
