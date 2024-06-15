def shift(lst):
     lst=lst[-2:]+lst[len(lst)-2:-1]+lst[:len(lst)-1]
     return
          

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

