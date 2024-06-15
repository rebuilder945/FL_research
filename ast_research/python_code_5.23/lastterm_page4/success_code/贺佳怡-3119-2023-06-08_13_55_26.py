a=eval(input())
b=len(a)
for i in range(0,b):
    if a.count(a[i])>1:
        del a[i]
print(a)
