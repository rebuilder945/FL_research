def add_id(data2):
    s=[]
    for x in data2:
        s.append('20'+x)
    return s 

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

