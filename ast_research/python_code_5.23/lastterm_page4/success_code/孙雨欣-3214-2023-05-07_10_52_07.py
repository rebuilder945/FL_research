a=eval(input())
b=a.count(0)
while a.count(0)>0:
    a.remove(0)
while b>0:
    a.append(0)
    b=b-1
print(a)
