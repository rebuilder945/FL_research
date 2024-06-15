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
l2=[]
for i in range(n):
    l2.append(a[i][-2:])
print(l1)
print(l2)
print("yes",dic.get("India","no"))
print(sum(l2))
