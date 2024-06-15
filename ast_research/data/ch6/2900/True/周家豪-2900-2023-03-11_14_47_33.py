def predition(n):
    if n==int(n) and n>1:
        return True
    else:
        return False
def sushu(a):
    if a==2:
        return True
    else:
        for i in range(2,a):
            if a%i==0:
                return False
        return True
def huiwenshu(a):
    a=str(a)
    b=a[::-1]
    if a==b:
        return True
    
n=eval(input())
lst=[]
if predition(n)==True:
    for i in range(2,n+1):
        if sushu(i)==True and huiwenshu(i)==True:
            lst.append(i)
    print(" ".join(str(i) for i in lst))
else:
    print("illegal input")

