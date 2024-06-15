def shift(lst):
    lst1=lst[::]
    for i in range(len(lst1)):
        if i == len(lst1)-1:
            lst[0]=lst1[-1]
            break
        lst[i+1]=lst1[i]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

