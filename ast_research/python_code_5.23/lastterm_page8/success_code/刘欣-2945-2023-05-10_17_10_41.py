def add_id(data2):
    lis1=[]
    for i in data2:
        i="20"+str(i)
        lis1.append(i)
    return lis1


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

