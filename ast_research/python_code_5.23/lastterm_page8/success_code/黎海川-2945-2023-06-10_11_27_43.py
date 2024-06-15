def add_id(data2):
    l=list(data2)
    for i in l:
        return '20'+str(i)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

