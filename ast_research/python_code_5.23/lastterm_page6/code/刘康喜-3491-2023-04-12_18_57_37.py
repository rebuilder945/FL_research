def shift(lst):
a=lst[0]
b=lst[-1]
c=[]
c.append(b)
for i in range(0,len(lst)-1):
    c.append(lst[lst[i]])
return c


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

