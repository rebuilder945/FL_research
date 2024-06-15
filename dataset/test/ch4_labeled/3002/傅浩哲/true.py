a=eval(input())
b=0
for i in a:
    b+=i
b=b/len(a)
if int(b)-b==0:
    print('%d'%b)
else:
    print('%.2f'%b)
