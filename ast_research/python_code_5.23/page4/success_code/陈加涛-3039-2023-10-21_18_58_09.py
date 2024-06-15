a=eval(input())
a.sort(reverse=False)
b=[]
for i in a:
    if i not in b:
        b.append(i)
del b[0]
del b[-1]
print(b)


