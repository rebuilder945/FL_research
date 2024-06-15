def shift(lst):
    ls=[lst[-1]]
    del lst[-1]
    ls.extend(lst)
    lst=ls

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

