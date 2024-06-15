def shift(lst):
    lst=list(lst)
    a=lst[0]
    for i in range(0,len(lst)-2):
        lst[i]=lst[i+1]
    lst[-1]=a
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

