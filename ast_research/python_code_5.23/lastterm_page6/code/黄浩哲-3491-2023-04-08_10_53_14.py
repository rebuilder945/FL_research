def shift(lst):
n = len(lst)
    temp = lst[n-1]
    for i in range(n-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = temp
    return lst


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

