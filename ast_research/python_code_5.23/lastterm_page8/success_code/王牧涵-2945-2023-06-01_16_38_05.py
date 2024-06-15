def add_id(data2):
            ids=[]
            for x in data2:
                    x=20000000+int(x)
                    ids.append(x)
            return ids      

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

