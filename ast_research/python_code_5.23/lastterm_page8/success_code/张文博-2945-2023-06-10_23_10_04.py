def add_id(data2):
    m=[]
    for x in data2:
            n='20'+x
            m.append(n)
    return m
               

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

