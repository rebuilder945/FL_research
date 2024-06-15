def add_id(data2):
    x=[]
    for i in range(len(data2)):
         x.append('20'+data2[i][:-1])
    return x

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

