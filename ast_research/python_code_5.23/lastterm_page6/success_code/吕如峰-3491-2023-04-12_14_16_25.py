def shift(lst):
  x=lst[1::-1]
  y=lst[:1:-1]
  return list(reversed(x+y))

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

