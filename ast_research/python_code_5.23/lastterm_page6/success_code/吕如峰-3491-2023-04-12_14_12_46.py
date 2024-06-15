def shift(lst):
  x=list(lst[1::])+list(lst[0])
  return x

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

