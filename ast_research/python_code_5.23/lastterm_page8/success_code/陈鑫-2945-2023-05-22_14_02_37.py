def add_id(data2):
    
    for i in data2:
        i.insert(0,0)
        i.insert(0,2)
    return data2

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

