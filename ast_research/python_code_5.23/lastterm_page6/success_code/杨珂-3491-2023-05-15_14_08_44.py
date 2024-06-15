def shift(lst):
   a=lst.pop()
   b=[a]
   for i in lst:
      b.append(i)
   return b


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

