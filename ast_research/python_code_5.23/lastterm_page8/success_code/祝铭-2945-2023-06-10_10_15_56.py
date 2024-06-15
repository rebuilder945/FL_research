def add_id(data2):
    li = []
    for i in data2:
        li.append(int(i)+20000000)
    return li

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

