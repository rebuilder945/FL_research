def add_id(data2):
    dataa=data2.copy()
    for i in data2:
        dataa.insert(0,20)
    return dataa

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

