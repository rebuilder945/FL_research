def shift(lst):
    a = list(lst)
    c = []
    c.append(a[-1])
    for x in a:
        if x not in a:
            c.append(i)
    return c

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

