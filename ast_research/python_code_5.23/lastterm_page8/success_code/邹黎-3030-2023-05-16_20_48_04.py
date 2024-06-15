mingzi=input().split(",")
fenshu=input().split(",")
lst0=[]
for x in range(0,len(mingzi)):
    lst0.append([mingzi[x],int(fenshu[x])])
lst0.sort(key=lambda x:x[1])
print(lst0)
