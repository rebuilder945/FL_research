def add_id(data2):
        lst=[]
        for i in data2:
            b='20'+i
            lst.append(b)
        return(lst)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

