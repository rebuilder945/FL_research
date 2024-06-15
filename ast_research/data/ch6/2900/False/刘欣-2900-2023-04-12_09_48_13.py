n=eval(input())
def sushu(x):
    if x<2:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
    return True
def huiwen(x):
    return str(x)==str(x)[::-1]
if (n-int(n))>0:
    print("illegal input")
elif n<=1:
    print("illegal input")
else:
    s=[]
    for i in range(2,n+1):
        if sushu(i) and huiwen(i):
            s.append(i)
        for i in s:
            print("%d"%i,end=" ")
     
