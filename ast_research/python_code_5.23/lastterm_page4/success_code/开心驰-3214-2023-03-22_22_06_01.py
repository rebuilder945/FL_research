a=eval(input())
b=a.count(0)
for i in range(b):
    b.remove(0)
    b.append(0)
print(b)
