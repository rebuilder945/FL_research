def add_id(data2):
    a=[]
    for i in data2:
        i+="20"
        a.append(i)
    rreturn a


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

