def shift(lst):
    a=len(list1)
    for i in range(0,a-1):
        list1[a-2-i],list1[a-1-i]=list1[a-1-i],list1[a-2-i]
    return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

