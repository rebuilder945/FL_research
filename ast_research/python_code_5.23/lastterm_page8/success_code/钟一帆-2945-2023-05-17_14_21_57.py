def add_id(data2):
    t='20'
    b=[]
    for i in data2:
        a=''
        a=t+i
        b.append(a)
    return b
        
        

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

