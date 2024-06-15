def shift(lst):
      length=len(lst)
      old=lst[length-1]
      for i in range (length-1,0,-1):
           lst[i]=lst[i-1]
      lst[0]=old

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

