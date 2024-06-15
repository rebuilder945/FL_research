def su(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i==0:
           return 0
    return 1
def huiwen(n):
    b=str(n)
    lst=list(b)
    lst2=lst.copy()
    lst.reverse()
    if lst==lst2:
        return 1
    else:
        return 0
s=eval(input())
if s<0 or type(s)!=int:
     print("illegal input")
else:
    lst=list(range(2,s+1))
    lst2=[]
    for x in lst:
        if huiwen(x)+su(x)==2:
            lst.append(x)
        for i in lst2:
            print(i,end='')


