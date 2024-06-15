lis=eval(input())
duo=[]
for x in lis:
    if lis.count(x)>=2:
        duo.append(x)
for n in duo:
    while lis.count(n)>=2:
        lis.remove(n)
print(lis)
