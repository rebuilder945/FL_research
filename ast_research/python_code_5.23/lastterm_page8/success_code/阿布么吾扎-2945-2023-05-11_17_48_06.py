def add_id(data2):
    ls=[]
    for x in data2:
        if len(x)<8:
            ls.append('20'+x)
        else:
            ls.append(x)


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

