def add_id(data2):
    a=data2.copy()
    for x in data2:
      a.insert(0,'20')
    return a

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

