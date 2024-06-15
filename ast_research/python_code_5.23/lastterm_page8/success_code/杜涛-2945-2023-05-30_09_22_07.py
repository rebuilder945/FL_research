def add_id(data2):
    a=[]
    for i in data2:
        a.append("20"+i)
    return a

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

