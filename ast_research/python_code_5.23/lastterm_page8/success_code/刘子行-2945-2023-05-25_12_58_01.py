def add_id(data2):
    ass=[]
    for x in data2:
        a="20"+x
        ass.append(a)
    return ass

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

