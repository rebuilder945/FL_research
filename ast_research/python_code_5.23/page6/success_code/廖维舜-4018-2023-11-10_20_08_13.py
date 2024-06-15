def shift(lst):
      tem=lst[-1]
      lst.insert(0,tem)
      lst.po(-1)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

