def add_id(data2):
    date3=[]
        for x in date1:
         if len(x)<8:
            date3.append("20"+x)
        else:
            date3.append(x)
        return date3


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

