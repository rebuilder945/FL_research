def shift(lst):
    a = lst.pop()
    list.insert(0,a)
    return a

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

