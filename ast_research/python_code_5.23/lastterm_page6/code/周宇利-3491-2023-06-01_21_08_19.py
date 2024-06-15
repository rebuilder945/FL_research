def shift(lst):
     for i in range(0,len(lst)-1):
          lst[i],lst[i+1]=lst[i+1],lst[i]
      return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

