def shift(lst):
    lst=list1
    a=lst.pop()
    lst.insert(0,a)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

