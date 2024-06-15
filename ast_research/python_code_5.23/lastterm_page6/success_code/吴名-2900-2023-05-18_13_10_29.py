def h(n):
    flag=True
    n=list(str(n))
    for i in range(len(n)):
        if n[i]!=n[-1-i]:
            flag=False
    if flag!=False:
        return True
    else:
        return False
def s(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
    if n==0 or n==1:
        flag=False
    if flag==True:
        return True
n=eval(input())
if type(n)==float or n<=0:
    print("illegal input")
else:
    for i in range(n):
        if h(i)==True and s(i)==True:
            print(i,end=" ")
