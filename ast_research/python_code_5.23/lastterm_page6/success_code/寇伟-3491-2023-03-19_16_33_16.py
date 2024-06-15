def shift(lst):
    for i in range(len(lst)-1):
        lst[i]=list[i+1]
        lst[-1]=0


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

