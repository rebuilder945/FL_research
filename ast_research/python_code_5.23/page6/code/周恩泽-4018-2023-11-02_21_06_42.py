def shift(lst):
a=lst[0]
    for i in range(1,len(lst)):
        lst[i-1]=lst[i]
    lst[-1]=a

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

