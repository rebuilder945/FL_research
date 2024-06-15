def shift(lst):
  x=_lst[0::-1]
  y=_lst[:0:-1]
  return list(reverse(x+y))

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

