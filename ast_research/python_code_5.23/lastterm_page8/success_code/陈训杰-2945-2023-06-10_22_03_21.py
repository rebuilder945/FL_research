def add_id(data2):
    data2=[]
    for x in data1:
        data2.append(20+x)
    return data2

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

