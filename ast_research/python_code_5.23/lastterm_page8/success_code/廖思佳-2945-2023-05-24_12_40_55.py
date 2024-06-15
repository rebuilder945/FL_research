def add_id(data2):
        list1=[]
        for i in data2:
            list1=list1+["20"+i]
        return list1    

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

