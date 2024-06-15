def add_id(data2):
    a=[]
    b="20"
    for i in data2:
        a.append(b+i)
    return a

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

