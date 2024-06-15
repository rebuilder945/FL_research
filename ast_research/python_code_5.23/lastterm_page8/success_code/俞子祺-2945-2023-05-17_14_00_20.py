def add_id(data2):
    for x in data2:
        list(x)
        x.insert(0,"2")
        x.insert(1,"0")
    return x

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

