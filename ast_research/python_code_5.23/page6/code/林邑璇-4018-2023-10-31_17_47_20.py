def shift(lst):
    a=len(list1)
    for i in range(a,-1):
        list1[a-1],list1[a]＝list1[a],list1[a-1]
    return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

