a=eval(input())
b=a.acount(0)
for x in range(b):
    a=a.remove(0)
for x in range(b):
    a=a.append(0)
print(a)



