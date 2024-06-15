def add_id(data2):
    ls=[]
    for i in data2:
        s='20'+str(i)
        ls.append(s)
    return ls

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

