def add_id(data2):
    v=[]
    for t in data2:
            if len(t)<8:
                v.append('20'+t)
            else:
                v.append(t)
    return(v)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

