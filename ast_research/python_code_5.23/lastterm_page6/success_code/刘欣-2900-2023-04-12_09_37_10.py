n=eval(input())
def sushu(x):
    if x<2:
        return False
    else:
        for i in range(2,n):
            if x/i==0:
                return False
    return True
def huiwen(x):
    if str(x)==str(x)[::-1]:
        return True
if (n-int(n))>0:
    print("illegal input")
elif n<0:
    print("illegal input")
else:
    s=[]
    for i in range(2,n):
        if sushu(n) and huiwen(n):
            s.append(i)
        for i in range(len(s)):
            print("%d"%s,end="")
     
