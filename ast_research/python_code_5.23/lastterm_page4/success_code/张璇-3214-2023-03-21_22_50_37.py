a=eval(input())
b=a.count(0)
while 0 in a:
    a.remove(0)
c=[0]
d=c*b
a.extend(d)
print(a)
