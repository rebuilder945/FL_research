def add_id(data2):
    for x in date2:
        x.reverse()
        x.append("02")
        x.reverse()
    return x

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

