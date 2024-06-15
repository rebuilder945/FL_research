def shift(lst):
for i in reversed(len(lst)):
      if i >0:
          lst[i]=lst1[i-1]
      else:
            lst[i]=lst1[-1]
return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

