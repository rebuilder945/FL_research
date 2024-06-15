a=eval(input())
a.sort()
b=[]
for i in range(len(a)):
    if a.count(a[i])==1:
        b.append(a[i])  
    c=[str(i) for i in b]
    d=','.join(c)
print(d)
if a.count(a[i])>1:
    print("False")
