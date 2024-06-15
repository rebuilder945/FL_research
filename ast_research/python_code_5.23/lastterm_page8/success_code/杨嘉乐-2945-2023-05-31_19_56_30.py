def add_id(data2):
    new=[]
    for i in data2:
        ii=i[::-1]+"02"
        new.append(ii[::-1])
    return new

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

