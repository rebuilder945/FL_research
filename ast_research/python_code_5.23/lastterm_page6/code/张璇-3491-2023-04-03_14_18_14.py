def shift(lst):
lst1=lst.copy()
    for x in range(len(lst1)):
        a=lst1[x-1]
        del lst[0]
        lst.extend(a)
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

