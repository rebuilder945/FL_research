def add_id(data2):
        result=[]
        data3=[data2]
        for x in data3:
            x.insert(0,'20'）
            result.append(x) 
            result.spilt()
        return result

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

