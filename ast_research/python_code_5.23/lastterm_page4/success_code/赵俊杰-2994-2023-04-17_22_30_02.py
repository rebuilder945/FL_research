ls=list(eval(input()))
a,b=eval(input())
s=len(ls)
if 1+a**2**(1/2)>s:
    print("error")
else:
    x=ls[a]
    while b>0:
        ls.append(x)
        b-=1
    print(ls)

