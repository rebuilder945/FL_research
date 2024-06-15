a=eval(input())
a.reverse()
b=[]
for x in a:
    if x in b:
        b=b
    else:
        b.append(x)
b.reverse()
print(b)
