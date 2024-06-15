n=eval(input())
x=2
y=1
l=[]
for i in range(n+1):
    x=x+y
    y=x
    a=x/y
    l.append(a)
s=sum(l)
print(s)
