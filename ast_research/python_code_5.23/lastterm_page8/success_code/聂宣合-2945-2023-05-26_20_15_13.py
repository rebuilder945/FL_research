def add_id(data2):
        lst=[]
        for r in data2:
            x="20"+str(r)
            lst.append(x)         
        return lst

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

