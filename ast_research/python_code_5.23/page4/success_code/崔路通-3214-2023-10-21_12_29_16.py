a=eval(input())
b=a.copy()
for x in b:
    if x==0:
        a.remove(0)
        a.append(0)
print(a)
