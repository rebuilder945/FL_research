a=eval(input())
b=[]
for x in a[::-1]:
    if x not in b:
        b.append(x)
print(b[::-1])
