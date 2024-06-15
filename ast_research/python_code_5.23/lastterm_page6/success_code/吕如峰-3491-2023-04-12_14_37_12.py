def shift(lst):
  for i in range(len(lst)):
    lst[i]=lst[i+1]
    lst[0]=lst[-1]
    return(lst)


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

