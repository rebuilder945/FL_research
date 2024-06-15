n=eval(input())
def sushu(x):
    for n in range(2,x//2+1):
        if x%n==0:
            return False
        else:
            return True
def huiwenshu(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False
n=eval(input())
if n>1:
    for x in range(n):
        if sushu(x) and huiwenshu(x):
            print(x,end=' ')
else:
    print("illegal input")
