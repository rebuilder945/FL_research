a=eval(input())
b=a.count(0)
while b>=1:
    a.remove(0)
c=[0]*b
a=a+c
print(a)
