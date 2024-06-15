def add_id(data2):
         ids=[]
         for i in data2:
                 i2='20'+i
                 ids.append(i2)
         return ids
            

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

