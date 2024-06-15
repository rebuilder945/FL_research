a=eval(input())
b=0
for i in a:
    b+=int(i)
c=b/len(a)
if c%1==0:
    print(c)
else:
    print('%.2f'%c)
