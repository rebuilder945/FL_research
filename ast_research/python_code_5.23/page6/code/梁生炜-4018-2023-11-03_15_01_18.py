def shift(lst):
lst1=lst.copy()
for i in range(len(lst)):
      if i >0:
          lst[i]=lst1[i-1]
      else:
            lst[i]=lst1[-1]
return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

