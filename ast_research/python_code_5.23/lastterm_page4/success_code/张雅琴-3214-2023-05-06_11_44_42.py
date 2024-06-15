a=eval(input())
b=a.count(0)
c=[0]*b
for i in a:
    if i==0:
        a.remove(i)
d=a+c
print(d)
