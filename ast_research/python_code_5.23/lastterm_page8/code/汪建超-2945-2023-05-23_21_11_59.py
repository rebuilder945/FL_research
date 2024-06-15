def add_id(data2):
    lst = []
    for x in data2:
        lst2 = [20]+x
        lst.append(lst2)
    s = *lst
    return s

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

