def shift(lst):

    lst2 = lst.copy()
    
    a = len(lst) - 1
    for x in lst:
        if a == len(lst) - 1:
            lst[a] = lst[a-1]
            a -= 1
        elif a == 0:
            break
        else:
            lst[a] = lst[a-1]
            a -= 1
    lst[a] = lst2[len(lst2)-1]
list1 = input().split(",")

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

