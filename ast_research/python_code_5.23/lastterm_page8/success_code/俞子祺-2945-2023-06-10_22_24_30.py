def add_id(data2):
    ls=[]
    for i in data2:
        i[0:3]=20
        ls.append(i)
    return ls

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

