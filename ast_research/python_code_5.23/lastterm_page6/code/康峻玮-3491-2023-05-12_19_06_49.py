def shift(lst):
    y = lst[-1]
    for x in range(len(lst)):
        lst[x+1]=lst[x]
    shift(lst)=lst.extend(0,'y')
    return shift(lst)


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

