def add_id(data2):
        lst=[]
        for i in range data2:
            b="20".join(i)
            lst.append(b)
        return(lst)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

