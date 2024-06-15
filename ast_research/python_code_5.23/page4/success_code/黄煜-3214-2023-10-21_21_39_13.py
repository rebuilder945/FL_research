a=eval(input())
b=a.count(0)
i=0
while i<b:
    a.remove(0)
    a.append(0)
    i=i+1
print(a)
