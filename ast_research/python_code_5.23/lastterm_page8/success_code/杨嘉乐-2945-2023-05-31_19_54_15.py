def add_id(data2):
    new=[]
    for i in data2:
        ii=i.reverse()+"20"
        new.append(ii.reverse())
    return new

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

