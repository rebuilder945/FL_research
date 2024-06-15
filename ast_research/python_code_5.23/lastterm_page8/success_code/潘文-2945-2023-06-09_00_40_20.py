def add_id(data2):
    lst1=[]
    for i in data2:
        lst1.insert(0,'20')
    return lst1

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

