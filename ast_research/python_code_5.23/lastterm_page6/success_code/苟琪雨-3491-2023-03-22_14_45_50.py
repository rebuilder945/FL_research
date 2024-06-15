def shift(lst):
    lst1=lst.copy()
    for i in range(len(lst)-1,0,-1):
        lst[i]=lst[i-1]
    lst[0]=lst1[-1]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

