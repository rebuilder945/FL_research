def shift(lst):
a=lst[-1]
long=len(lst)-1
while long>0:
      lst[long]=lst[long-1]
      long-=1
lst[0]=a

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

