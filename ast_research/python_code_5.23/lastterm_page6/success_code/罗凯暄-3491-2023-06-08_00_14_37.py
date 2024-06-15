def shift(lst):
     lst.pop(4)
     lst.insert(0,lst[4])

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

