list = list(range(1,n+1))
for i in range(len(list)-1,0,-1):
    list[i],list[0]=list[0],list[i]
print(list)
