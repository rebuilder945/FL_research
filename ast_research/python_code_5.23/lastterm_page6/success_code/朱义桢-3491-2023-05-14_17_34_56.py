def shift(lst):
    lis=lst[:]
    lst1=lis[-1]+lis[0,len(lst)-1]
    lst=lst1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

