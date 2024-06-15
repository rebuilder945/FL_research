def add_id(data2):
        result=[]
        for x in data2:
            x.insert(0,'20')
            result.append(x) 
        return result

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

