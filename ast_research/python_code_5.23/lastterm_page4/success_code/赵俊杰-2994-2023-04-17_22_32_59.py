ls=list(eval(input()))
a,b=eval(input())
s=len(ls)
if a>0:
    if 1+a>s:
        print("error")
    else:
        x=ls[a]
        while b>0:
            ls.append(x)
            b-=1
        print(ls)
else:
    if 1-a>s:
        print("error")
    else:
        x=ls[a]
        while b>0:
            ls.append(x)
            b-=1
        print(ls)

