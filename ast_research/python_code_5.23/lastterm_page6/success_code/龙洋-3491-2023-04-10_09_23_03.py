def shift(lst):
    y=lst.pop()
    lst.insert(0,y)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

