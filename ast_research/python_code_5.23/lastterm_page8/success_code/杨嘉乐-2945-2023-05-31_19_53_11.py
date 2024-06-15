def add_id(data2):
    new=[]
    for i in data2:
        i+="20"
        new.append(i)
    return new

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

