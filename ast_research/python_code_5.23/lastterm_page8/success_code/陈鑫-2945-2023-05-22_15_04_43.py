def add_id(data2):
    a='20'
    s=[]
    for i in data2:
        i=a+i
        s.append(i)
    return s

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

