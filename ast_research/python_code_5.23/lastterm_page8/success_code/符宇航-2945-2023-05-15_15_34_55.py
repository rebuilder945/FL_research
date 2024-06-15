def add_id(data2):
            data3=[]
            for i in data2:
                    if len(i)==8:
                            data3.append(i)
                    else:
                            i=str(i)
                            i='20'+i
                            data3.append(i)
            return data3

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

