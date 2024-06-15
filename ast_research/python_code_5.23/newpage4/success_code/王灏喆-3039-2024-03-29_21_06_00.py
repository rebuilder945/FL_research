name=eval(input())
a=max(name)
b=min(name)

while a in name:
 name.remove(a)
while b in name:
 name.remove(b)

name1=name
print(name1)

