a=eval(input())
a.reverse()
b=[]
for x in a:
    if x not in b:
        b.append(x)
b.reverse()
print(b)

