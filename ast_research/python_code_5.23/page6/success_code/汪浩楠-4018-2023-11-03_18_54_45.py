def shift(lst):
    for i in range(n-1):
        lst[i]=lst[i+1]
    lst[n-1]=1
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

