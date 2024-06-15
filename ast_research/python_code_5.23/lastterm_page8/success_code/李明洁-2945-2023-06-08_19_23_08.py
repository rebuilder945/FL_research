def add_id(data2):
        for x in list(range(len(data2))):
            data2[x].insert(0,"20")
        return data2

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

