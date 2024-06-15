def add_id(data2):
        l=[]
        for i in data2:
            a="20"+i
            l.append(a)
        return l

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

