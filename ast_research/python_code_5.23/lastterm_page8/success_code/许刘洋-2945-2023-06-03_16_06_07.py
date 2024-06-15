def add_id(data2):
    ls=[]
    for x in data2:
        x.insert(0,'20')
        ls.append(x)
    return ls

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

