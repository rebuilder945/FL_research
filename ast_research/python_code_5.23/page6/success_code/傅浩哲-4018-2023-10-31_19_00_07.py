def shift(lst):
    list(lst)
    a=[]
    a.append(lst[-1])
    for i in range(0,len(lst)-1):
        a.append(lst[i])
    lst=a
    return(lst)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

