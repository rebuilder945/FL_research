def add_id(data2):
    return ['20'+x for x in data2]

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

