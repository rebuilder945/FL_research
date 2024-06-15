def add_id(data2):
            xh=[]
            for i in data2:
                if len(i)==8:
                    xh.append(i)
                else:
                    i='20'+i
                    xh.append(i)
            return xh

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

