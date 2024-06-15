def add_id(data2):
    for x in data2:
        x.insert(0,'20')
    return x

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

