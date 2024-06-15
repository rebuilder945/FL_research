ls=list(eval(input()))
a,b=eval(input())
if a <= len(ls)-1:
    c=ls[a]
    d=[c]*b
    li=ls+d
    print(li)
else:
    print('error')
