def shift(lst):
    a=lst[-1]
        for i in range(len(lst)-1,0,-1):
            lst[i]=lst[i-1]
        lst[0]=a

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

