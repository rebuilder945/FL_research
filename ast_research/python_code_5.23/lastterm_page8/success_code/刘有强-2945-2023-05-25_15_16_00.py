def add_id(data2):
        data2=list(data2)
        data3=[]
        for x in data2:
            x = "20"+x
            data3.append(x)
        return data3

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

