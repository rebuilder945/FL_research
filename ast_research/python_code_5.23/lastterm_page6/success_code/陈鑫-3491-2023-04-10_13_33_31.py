def shift(lst):
    lst=list(map(int,lst))
    for i in range(len(lst)-1):
        lst[i+1]=lst[i]
    lst[1]=lst[-1]+1
    lst=list(map(str,lst))

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

