def add_id(data2):
    lst=[]
    for i in data2:
        i.insert(0,20)
    return lst

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

