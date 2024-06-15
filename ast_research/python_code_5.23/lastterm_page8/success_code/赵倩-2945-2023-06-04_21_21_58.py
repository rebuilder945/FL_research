def add_id(data2):
    c=[]
    for x in data2:
        b=20000000+x
        c.append(b)
    return c

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

