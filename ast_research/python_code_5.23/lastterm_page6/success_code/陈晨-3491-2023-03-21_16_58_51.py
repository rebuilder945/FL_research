def shift(lst):
    a=len(lst)
    lst.append(lst[len(lst)-1])
    for x in lst[0:len(lst)-1]:
        lst.append(x)
    while len(lst)!=a:
        lst.remove(lst[0])
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

