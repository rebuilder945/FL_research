def add_id(data2):
    list=[]
    for i in data2:
        a='20'+i
        list.append(a)
    return list

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

