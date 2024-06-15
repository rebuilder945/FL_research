def add_id(data2):
    a=[]
    for x in data2:
        x=str(20)+str(x)
        a.append(int(x))
    return a

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

