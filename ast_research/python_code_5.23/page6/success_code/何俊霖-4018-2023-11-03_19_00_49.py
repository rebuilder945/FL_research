def shift(lst):
    x = []
    for i in range(-2,-len(lst)-1,-1):
        x.append(lst[i])
    x.insert(0,x[-1])
    return x

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

