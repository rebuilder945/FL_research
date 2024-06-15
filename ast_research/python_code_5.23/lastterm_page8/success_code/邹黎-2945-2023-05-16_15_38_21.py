def add_id(data2):
    lst=[]
    a="20"
    for x in data2:
         b=a+x
         lst.append(b)
    return lst
        

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

