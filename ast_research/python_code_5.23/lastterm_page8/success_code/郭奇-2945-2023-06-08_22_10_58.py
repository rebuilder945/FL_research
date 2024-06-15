def add_id(data2):
    lst=[20]
    lst1=[]
    for i in data2:
        lst1.append(lst+i[0:6])
    return lst1

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

