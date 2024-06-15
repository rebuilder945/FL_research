def add_id(data2):
        dataa=[]
        for i in data2:
            i=int(i)
            i+=20000000
            dataa.append(i)
        return dataa

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

