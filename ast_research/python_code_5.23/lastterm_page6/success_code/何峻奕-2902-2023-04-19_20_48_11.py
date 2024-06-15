n=eval(input())
x=2
y=1
for i in range(n+1):
    x=x+y
    y=x
    a=x/y
s=sum(a)
print(s)
