def add_id(data2):
    ls=[]
    for x in data2:
        x=str(x)
        x='20'+x
        ls.append(x)
    return ls
        

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

