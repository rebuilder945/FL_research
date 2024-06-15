def add_id(data2):
    ls1 = []
    for i in data2:
        ls1.append("20"+i)
    return ls1

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

