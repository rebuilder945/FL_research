def add_id(data2):
    lst = list(data2)
    y = []
    for i in lst:
        if lst[0] != '2':
            x = '20' = i
            y.append(x)
        else:
            y.append(i)
    return y 

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

