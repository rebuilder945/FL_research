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
N = eval(input())
if N!=abs(int(N)):
    print("illegal input")
else:
    hui=[]
    m=2
    for x in range(2,N):
        if sushu(x) and reversenum(x) == x:
            hui.append(x)
    for x in range(len(hui)):
        print("%d "%hui[x],end='')
