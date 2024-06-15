def shift(lst):
    lenth=len(lst)
    for i in range(lenth):
        lst.append(lst(i))
    del lst[:lenth-2]
    lst.pop()

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

