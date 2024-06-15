def shift(lst):
      list2=[]
      for x in range(len(list1)):
         list2.append(x-1)
      return list2

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

