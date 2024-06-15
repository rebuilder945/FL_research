def add_id(data2):
    for i in data2:
        if i.startwith("19"):
            i.insert(0,20)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

