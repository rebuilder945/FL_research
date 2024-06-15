def add_id(data2):
    id=[]
    for i in data2:
        i=int(str("20")+str(i))
        id.append(i)
        return id

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

