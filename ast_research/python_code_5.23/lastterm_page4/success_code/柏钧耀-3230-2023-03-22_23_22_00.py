lst=eval(input())
m=[]

for i in range(len(lst)):
    j=max(lst)
    m.append(j)
    lst.remove(j)
if sum(m)==0:
    print("0")
else:
    n=''.join(str(i)for i in m)
    print(n)

