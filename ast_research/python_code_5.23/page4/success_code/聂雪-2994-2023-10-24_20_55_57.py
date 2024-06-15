ls=list(eval(input()))
a,b=eval(input())
if a <= len(ls)-1:
    c=ls[a]
    d=[c]*3
    li=ls+d
    print(li)
else:
    print('error')
