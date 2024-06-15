def add_id(data2):
        lst=[]
        for x in data2:
            x1='20'+x
            lst.append(x1)
        return lst

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

