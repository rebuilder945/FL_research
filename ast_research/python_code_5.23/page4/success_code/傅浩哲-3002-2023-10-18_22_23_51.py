a=eval(input())
b=0
for i in a:
    b+=i
b=b/len(a)
c='%.2f'%b
if str(c)[-1]==0 and str(c)[-2]==0:
    print('%d'%c)
else:
    print(c)
