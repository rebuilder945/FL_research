def add_id(data2):
    for x in data2:
        list(x).reverse()
        list(x).append('02')
        list(x).reverse()
    return data2

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

