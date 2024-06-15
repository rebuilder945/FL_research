def sushu(n):
    if n > 1:
        for i in range(2,n):
            if n % i ==0:
                return 0
    return 1
def huiwen(n):
    num=str(n)
    m=num[::-1]
    if num == m:
        return n
N=eval(input())
if N-int(N)>0:
    print("illegal input")
elif N<1:
    print("illegal input")
else:
    N=int(N)
    hui=[]
    m=2
    for i in range(2,N):
        if sushu(i)and huiwen(i)== i:
            hui.append(i)
    for i in  range(len(hui)):
       print("%d"%hui[i],end=' ')
