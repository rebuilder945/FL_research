def shift(lst):
    a=lst.copy()
    for i in range(len(a)):
        lst[i]=a[i-1]
    return lst


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

