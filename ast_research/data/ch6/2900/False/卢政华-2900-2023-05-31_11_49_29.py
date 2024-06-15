def sushu(n):
    if n>1:
        for i in range (2,n):
            if n%i==0:
                return 0
   
    return 1
def huishu(n):
    n1=str(n)
    n2=n1[::-1]
    if n2==n1:
        return n
n=float(input())
sums=[]
if n-int(n)>0:
    print("illegal input")
elif n<1:
    print("illegal input")
else:
    n=int(n)
    for i in range(2,n):
        if sushu(n) and huishu(n)==n:
            sums.append(n)
    for i in range (len(sums)):
        print("%d"%sums[i],end="")
