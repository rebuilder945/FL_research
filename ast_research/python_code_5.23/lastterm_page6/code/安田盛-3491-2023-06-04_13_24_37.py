def shift(lst):
for i in range(-1,-len(lst),-1):
        lst[i],lst[i-1]=lst[i-1],lst[i]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

