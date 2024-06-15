def shift(lst):
a=list[-1]
for i in range(len(list)-1,0,-1):
    list[i]=list[i-1]
list[0]=a

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

