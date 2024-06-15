def shift(lst):
    b = list1.pop()
    list1.insert(0,b)
    return b

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

