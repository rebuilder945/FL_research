def add_id(data2):
    lst=[]
    for i in data2:
        i_lst=list(x for x in i)
        i_lst.insert(0,20)
        i_out="".join(i_lst)
        lst.append(i_out)
    return lst

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

