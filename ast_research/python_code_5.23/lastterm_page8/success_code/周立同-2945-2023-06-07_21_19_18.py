def add_id(data2):
    lst=[]
    data2=list(map(int,data2))
    for i in data2:
        lst.append(i+20000000)
    return lst
        

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

