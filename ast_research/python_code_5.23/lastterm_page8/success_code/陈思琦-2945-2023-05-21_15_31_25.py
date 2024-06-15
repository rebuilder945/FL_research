def add_id(data2):
    a=' '
    b=str(20)
    for i in data2:
        id=b+i
        a+=id+' '
    return a.split()

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

