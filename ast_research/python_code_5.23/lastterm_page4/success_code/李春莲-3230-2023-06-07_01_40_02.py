l=eval(input())
l.sort(reverse=False)
l2=[]
s=0
for i in l:
    a=(i*(10**s))
    s+=1
    l2.append(a)
print(sum(l2))
