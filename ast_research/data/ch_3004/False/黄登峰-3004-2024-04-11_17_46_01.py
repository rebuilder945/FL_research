a=eval(input())
b=sum(a)
c=b/len(a)
d=str(c)
if d[2]==0:
    print(d[0])
else:
    print('{:.2f}'.format(c))
