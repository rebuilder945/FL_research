def shift(lst):
    a=lst[-1]
    for i in range(lst):
        remove.a()
        lst[i]=lst[i-1]
        lst=lst+a

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

