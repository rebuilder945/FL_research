def add_id(data2):
    ls=[]
    for x in data2:
        y=list(x)
        s=y.insert(0,20)
        a=str(s)
        ls.append(s)
    return ls
           

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

