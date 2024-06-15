def add_id(data2):
    ls2=[]
    for i in data1:
        a="20"+str(i)
        ls2.append(a)
    return ls2

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

