def shift(lst):
    x=list1.pop(-1)
    list1.insert(0,x)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

