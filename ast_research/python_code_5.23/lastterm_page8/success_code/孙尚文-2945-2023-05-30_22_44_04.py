def add_id(data2):
            c=[]
            for i in data2:
                    b="20"+str(i)
                    c.append(b)
            return c

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

