def shift(lst):
 b = len(lst)
    for i in range(b):
        if i == b-1:
            lst[i] = lst[0]
        elif i == 0:
            lst[i] = lst[b-1]
        else:
            lst[i] = lst[i+1]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

