def add_id(data2):
    b=[]
    for x in data2:
        a='20'+x
        b.append(a)
    return b

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

