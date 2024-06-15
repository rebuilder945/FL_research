def shift(lst):
    x = []
    for i in range(1,len(lst)):
        x.append(lst[i])
    x.append(lst[0])
    return x

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

