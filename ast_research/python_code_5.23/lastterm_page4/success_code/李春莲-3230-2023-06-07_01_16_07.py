l=eval(input())
l.sort(reverse=False)
l2=[]
s=0
for i in l:
    i=i*(10**(l[s]-1))
    s+=1
    l2.append(i)
print(sum(l2))
