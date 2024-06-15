def add_id(data2):
    data3 = []
    for t in data2:
        if len(x)<=8:
            data3.append("20"+t)
        else:
            data3.append(t)
        return data3

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

