def sushu(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def huiwensushu(x):
    if str(x)==str(x)[::-1]:
        return True
    return False
n=eval(input())
if n<=0 or type(n) != type(1):
    print("illegal input")
else:
    for a in range(2,n):
        if sushu(a) and huiwensushu(a):
            print(a,end=' ')
            

