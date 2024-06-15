def add_id(data2):
    l=[]
    for x in data2:
        l.append("20"+x)
    return l

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

