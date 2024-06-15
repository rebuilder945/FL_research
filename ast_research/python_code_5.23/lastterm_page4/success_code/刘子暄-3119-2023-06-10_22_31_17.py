a=eval(input())
b=[]
a.reverse()
for x in a:
    if x not in b:
        b.append(x)
        b.reverse()
print(b)

