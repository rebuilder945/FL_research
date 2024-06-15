def shift(lst):
    del list1[-1]
    list1.insert(0,'5')
    return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

