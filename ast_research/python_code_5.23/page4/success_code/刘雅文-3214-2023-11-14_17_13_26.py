'''a=eval(input())
for i in a:
    if i==0:
        del a[a.index(i)]
        a.append(i) 
print(a)'''


a=eval(input())
for x in a:
    if x==0:
        a.remove(x)
        a.append(x)
print(a)
