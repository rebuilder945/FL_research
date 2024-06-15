n = input().split(",")
g = input().split(",")
l1 = ()
l2=[]
for i in range(len(n)):
    l1=(n[i],g[i])
    l2.append(l1)
l2.sort(key=lambda x:x[1])
print(l2)
