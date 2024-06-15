def add_id(data2):
        d=[]
        for x in data2:
            d.append(str('20'+x))
        return(d)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

