def shift(lst):
list2 = list(lst[-1])
list3 = list2.append(lst)
lst = list3

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

