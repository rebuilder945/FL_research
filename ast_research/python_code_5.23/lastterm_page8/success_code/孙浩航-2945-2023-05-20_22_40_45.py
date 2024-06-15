def add_id(data2):
            kk=[]
            for a in data2:
                    b="20"+a
                    kk.append(b)
            return kk


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

