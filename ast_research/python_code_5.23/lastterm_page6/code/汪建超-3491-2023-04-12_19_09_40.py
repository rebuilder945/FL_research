def shift(lst):
lst = list.eval(input())
lst[1],lst[-1] = lst[-1],lst[1]
print(lst)


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

