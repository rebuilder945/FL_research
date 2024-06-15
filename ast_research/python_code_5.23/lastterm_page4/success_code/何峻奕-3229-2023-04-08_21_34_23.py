a=eval(input())
a.sort(reverse=True)
b=[]
for i in range(len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
        c=[str(i) for i in b]
        d=','.join(c)
        print(c)
    if a.count(a[i])>1:
        print("False")
