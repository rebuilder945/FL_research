def shift(lst):

    b = lst.pop(-1)
    lst.insert(0,b)
    for i in range(len(lst)):
        lst[i] = str(lst[i])

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

