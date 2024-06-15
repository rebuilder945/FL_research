def add_id(data2):
    a=[]
    for i in data2:
        if len(i)<8:
            a.append('20')
        else:
            a.append(i)
    return(a)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

