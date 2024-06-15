def add_id(data2):
    id =[]
    for x in data2:
         id.append("20"+x)
    return id

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

