def shift(lst):
    ls.insert(0,ls.pop())
    print(ls)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

