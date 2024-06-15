def add_id(data2):
    l=list(data2)
    for i in l:
        i.insert(20,0)
    return i

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

