end="ok"
a=[]
gdp=iter(input,end)
for x in gdp:
    a.append(x)
n=len(a)
dic={}
for i in range(n):
    dic[a[i][:-3]]=a[i][-2:]
l1=[]
for i in range(n):
    l1.append(a[i][:-3])
l1.sort()
l2=[]
for i in range(n):
    l2.append(int(a[i][-2:]))
l2.sort()
print(l1)
print(l2)
if "India" in l1:
    print("yes")
else:
    print("no")
print(sum(l2))
