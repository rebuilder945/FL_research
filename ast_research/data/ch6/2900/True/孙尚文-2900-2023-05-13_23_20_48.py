def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def huiwenshu(m):
    if str(m)==str(m)[::-1]:
        return True
    else:
        return False
a=eval(input())
if a<=1 or type(a)!=type(1):
    print("illegal input")
else:
    for i in range(2,a):
        if sushu(i) and huiwenshu(i):
            print(i,end=" ")
