def shift(lst):
    lis2=list(lst)
    a=lis2[4]
    lis3=lis2.pop(4)
    lis4=set(lis3).insert(0,a)
    lst=list(lis4)


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

