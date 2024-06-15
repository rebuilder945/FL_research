a=eval(input())
b=a.count(0)
while a.count(0) > 0:
    a.remove(0)
c=[0]*b
d=a+c
print(d)
