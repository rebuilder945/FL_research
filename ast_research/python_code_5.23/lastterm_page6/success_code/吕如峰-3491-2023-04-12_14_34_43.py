def shift(lst):
  lst[1]=lst[2]
  lst[2]=lst[3]
  lst[3]=lst[4]
  lst[4]=lst[5]
  lst[5]=lst[0]


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

