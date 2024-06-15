def add_id(data2):
    
    s=map(lambda x: '20' +x, data2)
    return s


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

