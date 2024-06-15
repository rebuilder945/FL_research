list=eval(input())
x=sum(list)
y=x/len(list)
z=int(y)
if not y-z:
    print(z)
else:
    print('%.2f'%(y))

