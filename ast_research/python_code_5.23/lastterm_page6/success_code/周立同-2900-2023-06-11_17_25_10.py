n=eval(input())
lst=[x for x in range(2,n+1)]
sulst=lst.copy()
for a in lst:
    for i in range(2,a):
        b=a%i
        if b==0:
            sulst.remove(a)
            break
        else:
            continue
sulst2=list(map(str,sulst))
lst1=sulst2.copy()
for m in sulst2:
    shu=list(m)
    for n in range(0,len(shu)):
        if shu[n]!=shu[len(shu)-n-1]:
            lst1.remove(m)
            break
str1=" ".join(lst1)
print(str1)
