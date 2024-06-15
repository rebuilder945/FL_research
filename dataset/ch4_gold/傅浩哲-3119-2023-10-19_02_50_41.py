a=eval(input())
b=[]
a.reverse()
for i in a:
    if i not in b:
        b.append(a)
b.reverse()
print(b)
