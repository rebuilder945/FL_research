def add_id(data2):
            c=[]
            for i in data2:
                if len(i)==6:
                    i="20"+i
                    c.append(i)
                else:
                    i=i
                    c.append(i)
            return c

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

