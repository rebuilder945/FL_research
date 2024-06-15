a=list(eval(input()))
b=a.count(0)
for i in range(b):
    a.remove(0)
for i in range(b):
    a=a+[0]
print(a)

