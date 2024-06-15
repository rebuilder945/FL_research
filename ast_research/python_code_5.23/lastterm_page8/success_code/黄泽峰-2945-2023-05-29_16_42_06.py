def add_id(data2):
    for x in data2:
        if len(x)<8:
            ls = ["20",x]
            x = ("".join(ls))
            return x

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

