def add_id(data2):
        ids = []
        for x in data2:
            if len(x) == 8:
                ids.append(x)
            else:
                 x = '20' + x
                 ids.append(x)
        return ids    

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

