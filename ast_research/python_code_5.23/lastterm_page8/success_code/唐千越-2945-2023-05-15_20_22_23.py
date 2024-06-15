def add_id(data2):
    id = ["20" + x for x in data2]
    return id

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

