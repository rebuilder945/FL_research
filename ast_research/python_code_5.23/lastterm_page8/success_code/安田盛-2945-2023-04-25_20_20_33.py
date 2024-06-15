def add_id(data2):
    x=["20"+i for i in data2]
    return x

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

