def F1(n):
    if n==2:
        return(True)
    for i in range(2,n):
        if n%i==0:
            return(False)
            
def F2(n):
    b = str(n)
    if b[::-1] == b:
        return(True)

a=eval(input())
b=[]
c=int(a)
if a!=c:
    print('illegal input')
elif c<0:
    print('illegal input')
else:
    for i in range(2,c+1):
        if F1(i)!=False:
            if F2(i)==True:
                b.append(i)
    for i in b:
        print(i)
