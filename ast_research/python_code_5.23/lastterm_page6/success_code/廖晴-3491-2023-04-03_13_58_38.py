def shift(lst):
    a=len(lst)
    b=lst[-1]
    for x in range(-1,-a,-1):
        lst[x]=lst[x-1]
    lst[-a]=b
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

