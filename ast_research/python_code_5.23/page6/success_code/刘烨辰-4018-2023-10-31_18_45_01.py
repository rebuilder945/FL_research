def shift(lst):
    a = list1[4]
    list1.insert(0,a)
    del list1[5]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

