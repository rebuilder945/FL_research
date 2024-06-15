a=eval(input())
a.reverse()
b=[]
for i in a:
    if a not in b:
        b.append(i)
print(b.reverse())
