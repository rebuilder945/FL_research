def shift(lst):
    m=lst[-1]
    lst.insert(0,m)
    lst.pop(-1)
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

