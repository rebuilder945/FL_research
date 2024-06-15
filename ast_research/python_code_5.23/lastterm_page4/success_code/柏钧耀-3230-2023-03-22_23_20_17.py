lst=eval(input())
m=[]

for i in range(len(lst)):
    j=max(lst)
    m.append(j)
    lst.remove(j)
n=''.join(str(i)for i in m)
print(n)

