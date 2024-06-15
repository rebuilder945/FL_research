def add_id(data2):
    lst=[]
    for i in data2:
        new='20'+str(i)
        lst.append(lst)
    return lst

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

