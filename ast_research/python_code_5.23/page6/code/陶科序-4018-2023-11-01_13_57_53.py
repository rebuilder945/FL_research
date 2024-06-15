def shift(lst):
    for i in range(len(lst)，0，-1):
        lst[i],lst[i-1] = lst[i-1],lst[i]
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

