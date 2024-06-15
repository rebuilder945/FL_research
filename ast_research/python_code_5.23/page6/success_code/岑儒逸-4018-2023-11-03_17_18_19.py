def shift(lst):
    lst=list(lst)
    a=lst[-1]
    lst.pop()
    lst.insert(0,a)
    lst1=lst
    return lst1
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

