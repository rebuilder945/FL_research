def add_id(data2):
    lst=[]
    for x in data2:
            lst.append('20'+x[0:6])
    return lst

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

