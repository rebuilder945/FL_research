a=eval(input())
b=sum(a)
c=b/len(a)
d='%.2f'%(c)
e=int(c)
if d/e==1.00:
    print(e)
else:
    print(d)
