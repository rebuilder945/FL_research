a=list(eval(input()))
b=max(a)
x=a.count(b)
for i in range(0,x):
    a.remove(b)
c=min(a)
y=a.count(c)
for i in range(0,y):
    a.remove(c)
print(a)
