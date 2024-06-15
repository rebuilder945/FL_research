def shift(lst):
     for x in range(1):
          lst.insert(0,list1.pop())
     return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

