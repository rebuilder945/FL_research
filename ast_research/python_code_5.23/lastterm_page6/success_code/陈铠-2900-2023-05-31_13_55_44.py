def su(n):
    if n<2:
        return False
    if n ==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
    return True
def hui(n):
    if str(n)==str(n)[::-1]:
        return True
    return False
n=eval(input())
if n<=0 or int(n)<n:
    print("illegal input")
else:
    lst=[]
    for i in range(1,n+1):
        if su(i) and hui(i):
            lst.append(i)
    for i in lst:
        print(i,end=" ")
