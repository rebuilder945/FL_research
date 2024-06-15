def shift(lst):

    a=lst[0]
    b=lst[-1]
    c=lst.copy()


    for i in range(0,len(lst)):
        lst[i]=c[i-1]
    return lst


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

