def add_id(data2):
    b='20'
    t=[]
    for x in data2:
        x=x+b
        t.append(x)
    return t

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

