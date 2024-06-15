def add_id(data2):
    lst1=[20]
    lst2=[]
    for i in data2:
        lst=lst1+i[0:6]
        lst2.append(lst[0])
    return lst2

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

