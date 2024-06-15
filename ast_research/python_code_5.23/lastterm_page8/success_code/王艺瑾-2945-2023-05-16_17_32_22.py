def add_id(data2):
    for i in data2:
        a=[]
        y="20"+i
        a.append(y)
    return a

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

