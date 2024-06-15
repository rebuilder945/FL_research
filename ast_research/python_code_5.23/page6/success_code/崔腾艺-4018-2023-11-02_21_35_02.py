def shift(lst):
    b=len(lst)
    c=lst.pop(b-1)
    lst.insert(0,c)
    return

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

