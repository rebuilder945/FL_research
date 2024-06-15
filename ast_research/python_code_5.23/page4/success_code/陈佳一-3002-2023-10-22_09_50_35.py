a=eval(input())
b=0
for i in a:
    b+=i
c=b/len(a)
if c%1!=0:
    print("c.2f")
else:
    print("c.d")
