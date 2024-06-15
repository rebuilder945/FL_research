def add_id(data2):
        ls=[]
        for i in data2:
            new="20"+i
            ls.append(new)
        return ls

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

