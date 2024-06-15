def add_id(data2):
    res = []
    for x in data1:
        res.append("20" + x)
    return res

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

