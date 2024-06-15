def add_id(data2):
    tmp=[]
    for x in data2:
        tmp.append("20"+x)
    return tmp

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

