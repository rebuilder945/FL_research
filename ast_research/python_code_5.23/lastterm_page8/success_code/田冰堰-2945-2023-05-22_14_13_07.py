def add_id(data2):
    return map(lambda s:'20'+s,data2)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

