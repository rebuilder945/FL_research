def add_id(data2):
    b=[]
    for i in data2:
        b.append('20'+str(i))
    return b

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

