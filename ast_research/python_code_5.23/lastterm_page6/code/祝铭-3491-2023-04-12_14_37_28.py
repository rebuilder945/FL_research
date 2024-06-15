def shift(lst):
    x = lst[-1]
    lst.pop()
    lst.assert(0,x)
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

