def add_id(data2):
        data3=[]
        for x in data2:
            y=int("20"+str(x))
            data3.append(y)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

