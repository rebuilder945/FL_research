a=eval(input())
b=0
for i in a:
    b+=i
c=b/len(a)
d=c-int(c)
if d==0:
    print(int(c))
else:
    print("%.2f"%c)
