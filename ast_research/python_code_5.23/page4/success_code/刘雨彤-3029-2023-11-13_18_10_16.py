a=input().split(",")
g =eval(input())
lst=[]
for i in range(len(a)):
    item=[]
    item.append(a[i])
    item.append(g[i])
    lst.append(item)
print(lst)     
