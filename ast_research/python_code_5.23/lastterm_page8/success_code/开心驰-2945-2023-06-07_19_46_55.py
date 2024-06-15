def add_id(data2):
    a=[]
    for i in range(len(data2)):
      a.append('20'+data2[i][0:6])
    return a

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

