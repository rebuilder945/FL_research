def add_id(data2):
            c=[]
            for x in data1:
                x=int(x)+20000000
                c.append(x)
            return c

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

