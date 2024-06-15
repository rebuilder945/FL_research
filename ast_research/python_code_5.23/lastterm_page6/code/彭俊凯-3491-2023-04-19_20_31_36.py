def shift(lst):
    b=[lst[-1]]
    for i in range(len(lst)-1):
        b.append(lst[i])
     return b

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

