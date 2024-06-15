def shift(lst):
      for i in range(len(list1)-2):
            list1[i+1]=list1[i]
            list1[0]=list1[-1]
      return(list1)


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

