def add_id(data2):
    for i in data2:
        i = "20"+i
    return i

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

