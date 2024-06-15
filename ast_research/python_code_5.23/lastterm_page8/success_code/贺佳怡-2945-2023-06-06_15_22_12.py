def add_id(data2):
    lis1=[20]
    for i in data2:
          lis1.append(i[:8])
    return lis1

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

