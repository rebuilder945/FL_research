def add_id(data2):
    ls=['20'+x for x in data2]
    return ls
        

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

