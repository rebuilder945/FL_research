def sushu(n):
    if n == 2:
        return 1
    else: 
        for i in range (2,n):
            if n%i==0:
                return 0
            elif i == n-1:
                return 1

def huishu(n):
    n1=str(n)
    n2=n1[::-1]
    if n2==n1:
        return True

n=eval(input())
sums=[]
if n <= 1:
    print("illegal input")
elif type(n) == float:
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i) == True and huishu(i) == True:
            sums.append(i)
    for i in range (len(sums)):
        print("%d"%sums[i],end=" ")
