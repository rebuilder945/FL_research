def shift(lst):
 list1 = input().spilt()
 a = list1[-1].spilt("")
 del list1[-1]
 list1 = a + list1 
 return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

