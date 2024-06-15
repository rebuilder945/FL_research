from math import sqrt
def p(x):
    f=True
    i=2
    while i<=sqrt(x):
        if x%i ==0:
            f=False
        i=i+1
    return f
def q(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
n=eval(input())
if n==float or n<0:
    input("illegal input")
else:
    n=int(n)
    ls=[]
    m=2
    while m<n:
        if p(m) == True and q(m) == True:
         ls.append(m)
        m+=1
    for x in ls:
        print(x,end = " ")

