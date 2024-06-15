def add_id(data2):
    lst1=[]
    for x in data2:
     lst1.append("20"+x)
    return lst1

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

