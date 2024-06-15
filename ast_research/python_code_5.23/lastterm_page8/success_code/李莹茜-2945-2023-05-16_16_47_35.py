def add_id(data2):
        ls=[]
        for x in data2:
            y="20"+str(x)
            ls.append(y)
        return ls

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

