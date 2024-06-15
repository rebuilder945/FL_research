n=eval(input())
a=0
for i in n:
    a+=i
b=len(n)
c=a/b
d=int("%d"%(c))
if c-d==0:
    print(d)
else:
    print("%.2f"%(c))
