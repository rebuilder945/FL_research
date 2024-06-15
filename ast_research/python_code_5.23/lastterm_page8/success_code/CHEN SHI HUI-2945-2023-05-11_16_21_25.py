def add_id(data2):
    x=[]
    for i in data2:
        x.append('20'+i)
    return x

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

