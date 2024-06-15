def shift(lst):
   lst1 = []
    lst1.append(lst[-1])
    for i in lst[:-1]:
        lst1.append(i)
    lst = lst1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

