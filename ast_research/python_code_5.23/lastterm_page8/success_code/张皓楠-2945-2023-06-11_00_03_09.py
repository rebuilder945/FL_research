def add_id(data2):
            m=[]
            for i in data2:
                m.append(20000000+int(i))
            return m

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

