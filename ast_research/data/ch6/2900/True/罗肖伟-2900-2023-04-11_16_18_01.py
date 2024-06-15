def abc(x):
    a=0
    for i in range(2,x):
        if x%i==0:
            a+=1
    if a==0:
        return 1
    else:
        return 0
n=eval(input())
if type(n)!=int or n<0:
    print("illegal input")
else:
    ls=[]
    x=2
    while x<n:
        ls1=str(x)
        ls2=ls1[::-1]
        if ls1==ls2 and abc(x)==1:
            ls.append(x)
        x+=1
    if len(ls)==0:
       print("illegal input")
    else:
       ls=str(ls)
       ls=ls.strip("[]")
       ls=ls.replace(",","")
       print(ls)


