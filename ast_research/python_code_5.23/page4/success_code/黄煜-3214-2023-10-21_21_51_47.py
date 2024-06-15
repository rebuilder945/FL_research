a=eval(input())
b=a.count(0)
for i in a:
    if i<=b:
        a.remove(0)
        a.append(0)
        i=i+1
print(a)

