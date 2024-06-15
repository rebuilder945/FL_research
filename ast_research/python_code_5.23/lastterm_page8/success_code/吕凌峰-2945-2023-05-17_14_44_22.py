def add_id(data2):
    d=[]
    for x in data2:
       f="20"+x
       d.append(f)
    return  d

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

