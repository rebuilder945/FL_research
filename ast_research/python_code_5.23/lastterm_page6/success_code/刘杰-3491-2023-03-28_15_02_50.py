def shift(lst):
    list=lst.copy
    del lst[-1]
    lst.insert(0,list[1])

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

