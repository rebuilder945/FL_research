def add_id(data2):
    xiu=[]
    for x in data2:
     n="20"+x
     xiu.append(n)
    return xiu

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

