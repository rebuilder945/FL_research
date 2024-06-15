def add_id(data2):
    result=[]
    for t in data2:
        if len(t)<=8:
            result.append("20"+t)
        else:
            result.append(t)
    return result

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

