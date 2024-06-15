n=eval(input())
a=n.count(0)
for x in range(a):
    n.remove(0)
b=[0]*a
c=n+b
print(c)
