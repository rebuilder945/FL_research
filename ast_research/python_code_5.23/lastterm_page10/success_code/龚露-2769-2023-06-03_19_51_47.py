a=input()
b=a[:]
print(b)
ls1='abcdefghijklmnopqrstuvwxyz'
ls2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in a:
    if x in ls1:
        a.replace(x,ls1[abs((25-ls1.find(x)))])
    elif x in ls2:
        a.replace(x,ls2[abs((25-ls1.find(x)))])
    print(a)
    
    
