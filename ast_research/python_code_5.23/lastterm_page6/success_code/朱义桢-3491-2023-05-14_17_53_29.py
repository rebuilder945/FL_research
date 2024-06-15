def shift(lst):
    lst2=lst[:]
    for i in range(len(lst)):
        lst[i]=lst2[i-1]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

