a=eval(input())
b=[i for i in range(1,a+1)]
for x in range(1):
    c=b.pop(0)
    b.append(c)
print(b)
