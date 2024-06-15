def add_id(data2):
    ls=[]
    for x in data2:
        s=x.insert(0,20)
        ls.append(s)
    return ls

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

