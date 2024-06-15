a=eval(input())
b=0
for i in a:
    b+=i
b=b/len(a)
c='%.2f'%b
if str(c)[-1]!=0 or str(c)[-2]!=0:
    print(c)
else:
    print('%.'%c)
