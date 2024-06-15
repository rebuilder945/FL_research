def add_id(data2):
        ls = []
        for x in data2:
            ls.append("2"+"0"+x[0:7])
        return ls

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

