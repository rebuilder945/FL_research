def add_id(data2):
    for x in data2:
        new='20'.__add__(x)
        return new

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

