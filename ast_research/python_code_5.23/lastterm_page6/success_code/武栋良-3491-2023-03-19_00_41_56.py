def shift(lst):
     n = len(lst)
     lst1 = lst[n-1:n]
     lst2 = lst[0:n-1]
     lst3 = lst1+lst2
     lst.copy(lst3)


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

