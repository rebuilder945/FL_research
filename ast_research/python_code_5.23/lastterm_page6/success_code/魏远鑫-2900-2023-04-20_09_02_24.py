n=eval(input())
def sushu(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True
def huiwen(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False
if n<=1 or n-int(n)!=0:
    print("illegal input")
else:
    for i in range(2,n+1):
        if sushu(i) and huiwen(i):
            print(i,end=" ")

