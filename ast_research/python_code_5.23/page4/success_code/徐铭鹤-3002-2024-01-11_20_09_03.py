a=eval(input())
b=0
for i in a:
    b+=int(i)
c=b/len(a)
if type(c)==int:
    print(c)
else:
    print('%.2f'%c)
