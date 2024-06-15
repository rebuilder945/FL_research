def shift(lst):
a = list(lst)
    list1 = []
    list1.append(a[-1])
    for i in range(0,len(a)-1):
        list1.append(a[i])
    print(list1)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

