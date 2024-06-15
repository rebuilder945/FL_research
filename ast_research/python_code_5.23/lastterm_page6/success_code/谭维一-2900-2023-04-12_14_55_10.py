def sushu(n):
    for i in n:
        if i>=2:
            for j in range (2,i):
                if i%j == 0:
                    return(0)
                else:
                    return n
def reversenum(n):
    num = str(n)
    m=num[::-1]
    if num==m:
        return n 
N = float(input())
if (N-int(N))>0:
    print("illegal input")
elif int(N)<1:
    print("illegal input")
else:
    N=int(N)
    hui=[]
    m=2
    for x in range(2,N):
        if sushu(x) and reversenum(x) == x:
            hui.append(x)
    for x in range(len(hui)):
        print("%d "%hui[x],end='')

