def shift(lst):
 b=lst[-1]
    for a in range(len(lst)-1,0,-1):
        lst[a]=lst[a-1]
    lst[0]=b

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

