def add_id(data2):
        for x in data2:
            x=list(x)
            x.reverse()
            x.append("20")
            x.reverse()
        return x

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

