def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def huiwenshu(n):
    num=str(n)
    m=num[::-1]
    if num==m:
        return n
n=eval(input())
if (n-int(n)>0) or int(n)<1:
    print("illegal input")
else:
    n=int(n)
    l=[]
    for x in range(2,n):
        if sushu(x) and huiwenshu(x):
            l.append(x)
    for i in range(len(l)):
        print(l[i],end=" ")

