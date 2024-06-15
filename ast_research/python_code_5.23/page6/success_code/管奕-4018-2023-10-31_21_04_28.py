def shift(lst):
    a=list(lst)
    del a[1]
    b=a[1]
    a.append(b)
    return a

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

