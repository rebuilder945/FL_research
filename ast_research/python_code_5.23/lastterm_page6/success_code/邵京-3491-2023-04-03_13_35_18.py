def shift(lst):
    for i in range(0,len(lst)):
        if i<len(lst)-1:
            lst[i+1]=lst[i]
        elif i==len(lst)-1:
            lst[i]=lst[0]
    return(lst)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

