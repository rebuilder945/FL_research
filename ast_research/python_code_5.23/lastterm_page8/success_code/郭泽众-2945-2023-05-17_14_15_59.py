def add_id(data2):
        plst = []
        for x in data2:
            cox = '20' + x
            plst.append(cox)
        return plst

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

