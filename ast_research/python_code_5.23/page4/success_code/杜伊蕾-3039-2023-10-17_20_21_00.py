a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
d=max(a)
e=min(a)
a.remove(d)*b
a.remove(e)*c
print(a)
