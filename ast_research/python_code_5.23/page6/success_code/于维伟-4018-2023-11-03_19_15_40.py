def shift(lst):
      list1.insert(0,list1.pop())
      return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

