def shift(lst):
x=0     
      while x<len(lst):
           lst[x]=lst[x-1]
           x=x+1
         

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

