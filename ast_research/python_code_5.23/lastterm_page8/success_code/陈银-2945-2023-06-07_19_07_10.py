def add_id(data2):
    new=[]
    for x in data2:
        m = "20"+x
        new.append(m)
    return new

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

