def add_id(data2):
    ls=[]
    for i in data2:
         k="2019"+str(i)
         ls.append(k)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

