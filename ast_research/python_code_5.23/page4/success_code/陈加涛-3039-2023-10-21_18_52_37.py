a=eval(input())
a.sort(reverse=True)
b=[]
for i in a:
    if i not in b:
        a.append(i)
del a[0]
del a[-1]
print(a)


