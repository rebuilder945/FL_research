def add_id(data2):
            a=[]
            for i in data2:
                    c='20'+i
                    a.append(c)
            return a

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

