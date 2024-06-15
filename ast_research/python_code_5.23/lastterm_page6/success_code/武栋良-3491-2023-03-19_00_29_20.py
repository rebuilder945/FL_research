def shift(lst):
     n = len(lst)
     lst1 = lst[n:]
     lst2 = lst[0:n]
     lst3 = lst1+lst2
     return lst3


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

