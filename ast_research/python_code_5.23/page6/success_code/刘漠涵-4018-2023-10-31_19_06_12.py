def shift(lst):
    a=len(lst)
    lst+=list(lst[0:-1])
    del lst[0:a-1]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

