x=eval(input())
b=x.count(0)
for i in range(b):
    x.remove(0)
for i in range(b):
    x.append(0)
print(x)
