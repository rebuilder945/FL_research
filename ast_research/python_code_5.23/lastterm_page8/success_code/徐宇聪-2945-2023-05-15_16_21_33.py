def add_id(data2):
    result = [x.insert(0,20) for x in data2]
    return result

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

