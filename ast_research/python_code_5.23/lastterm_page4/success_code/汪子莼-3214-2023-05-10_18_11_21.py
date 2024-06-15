a=eval(input())
n=a.count(0)
while a.count(0)>0:
    a.remove(0)
b=[0]*n
a=a+b
print(a)
