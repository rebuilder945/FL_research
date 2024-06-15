def shift(lst):
for i in range(len(lst)-2,-1,-1):
lst[i+1] = lst[i]
lst[0] = str(len(lst))
return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

