def shift(lst):
c=lst[-1]
 del lst[-1]
 lst.insert(0,c)
 for i in range(len(lst)):
  lst[i]=str(lst[i]) 
  

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

