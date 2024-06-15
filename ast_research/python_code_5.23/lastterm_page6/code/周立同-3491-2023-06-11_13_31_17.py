def shift(lst):
lst2=[]
for i in range(len(lst)-1,-1,-1):
    lst2.append(str(lst[i]))
return lst2

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

