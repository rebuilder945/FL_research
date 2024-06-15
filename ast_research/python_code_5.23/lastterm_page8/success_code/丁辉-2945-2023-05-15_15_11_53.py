def add_id(data2):
    a=[]
    for i in data2:
        i="20"+i
        a.append(i)
    return a


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

