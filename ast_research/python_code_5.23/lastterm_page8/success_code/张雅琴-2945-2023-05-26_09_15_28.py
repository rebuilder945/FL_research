def add_id(data2):
    result=[]
    for i in data2:
       result.append("20"+i)
    return result

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

