def shift(lst):
    for i in range(len(lst)):
        if i<len(lst):
            lst[i+1]=lst[i]
        else:
            lst[i]=lst[0]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

