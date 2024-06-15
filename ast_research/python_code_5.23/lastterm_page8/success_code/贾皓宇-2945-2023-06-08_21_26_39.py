def add_id(data2):
    b='20'
    for x in data2:
        x=x+b
    return x

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

