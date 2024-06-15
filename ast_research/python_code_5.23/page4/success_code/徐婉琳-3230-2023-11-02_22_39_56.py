c=eval(input())
c.sort(reverse=True)
if max(c)>0:
    print(*c,sep='')
else:
    print(0)
