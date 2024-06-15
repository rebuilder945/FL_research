def shift(lst):
    lst0=[lst[-1]]
    for i in range(len(lst)-1):
        lst0.append(lst[i])
    list1=lst0
    return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

