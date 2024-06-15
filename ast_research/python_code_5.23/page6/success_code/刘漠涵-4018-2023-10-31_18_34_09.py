def shift(lst):
    a=[lst[-1]]
    lst1=list(lst)
    del lst1[-1]
    lst=a+lst1
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

