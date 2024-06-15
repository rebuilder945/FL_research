def shift(lst):
list1 = list.lst
list1[1],list1[-1] = list1[-1],list1[1]
return list1


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

