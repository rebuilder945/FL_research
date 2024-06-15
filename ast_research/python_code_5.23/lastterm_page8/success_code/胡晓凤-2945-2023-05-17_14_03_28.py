def add_id(data2):
        data2=list(data2)
        ls=[]
        for x in data2:
            x="20"+str(x)
            ls.append(x)
        return ls

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

