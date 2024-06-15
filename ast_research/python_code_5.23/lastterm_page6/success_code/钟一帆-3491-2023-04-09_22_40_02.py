def shift(lst):
    lis2=list(lst)
    a=lis2[4]
    lis2.pop(4)
    lis4=lis2.insert(1,a)
    lst=lis4


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

