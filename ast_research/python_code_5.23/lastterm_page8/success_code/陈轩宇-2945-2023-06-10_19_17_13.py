def add_id(data2):
        list2=[]
        list1 = list(map(int,data2))
        for i in list1:
            i+=20000000
            list2.append(i)
        return list2

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

