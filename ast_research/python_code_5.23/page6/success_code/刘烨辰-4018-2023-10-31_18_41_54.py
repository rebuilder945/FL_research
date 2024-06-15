def shift(lst):
    a = list1[0]
    list1.append(a)
    del list1[0]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

