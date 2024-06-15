def add_id(data2):
        mm = []
        for i in data2:
            nn =["20",i]
            t = "".join("%s"%id for id in nn)
            mm.append(t)
        return mm

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

