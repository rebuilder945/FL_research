a=eval(input())
for i in range(0,len(a)):
    if type(a[i])==bool:
        a[i]=str(a[i])
b=a.copy()
for x in a:
    while b. count(x)>1:
        b.remove(x)
for i in range(0,len(b)):
    if b[i]=='True'or b[i]=='False':
        b[i]=eval(b[i])
print(b)
