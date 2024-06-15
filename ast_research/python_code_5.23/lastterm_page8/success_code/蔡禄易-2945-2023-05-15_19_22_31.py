def add_id(data2):
    n = [ ]
    for i in data2:
        i = str(20) + str(i)
        n.append(i)
    return n

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

