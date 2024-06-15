def add_id(data2):
    result = []
    for x in data2:
        result.append('20' + str(x))
    return result

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

