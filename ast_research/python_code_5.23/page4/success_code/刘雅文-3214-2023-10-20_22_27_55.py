a=eval(input())
for i in a:
    if i==0:
        del a[a.index(i)]
        a.append(i) 
print(a)
