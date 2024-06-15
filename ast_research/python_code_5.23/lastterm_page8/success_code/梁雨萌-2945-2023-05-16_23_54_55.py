def add_id(data2):
            lis=[]
            for i in data2:
                word = "20" + str(i)
                lis.append(word)
            return lis
     

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

