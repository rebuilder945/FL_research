def shift(lst):
    lst=list(lst)
    a=lst[-1]
    b=lst[0]
    for i in range(0,len(lst)-1):
        m=lst[i-1]
        lst[i]=m
    lst[0]=a
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

