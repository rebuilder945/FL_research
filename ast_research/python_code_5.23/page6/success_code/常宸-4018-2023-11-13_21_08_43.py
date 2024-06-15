def shift(lst):
    a=lst.pop(0)
    lst.remove(0)
    lst.append(a)
    print(lst)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

