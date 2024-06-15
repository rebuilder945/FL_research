def add_id(data2):
    lis1=[]
    for i in data2:
          lis1.append('20'+i[:6])
    return lis1

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

