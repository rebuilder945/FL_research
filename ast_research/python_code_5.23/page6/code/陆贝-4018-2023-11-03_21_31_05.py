def shift(lst):
    a=list(lst[-1]
    for i in lst[0:-1]:
        a.append(i)
    return a

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

