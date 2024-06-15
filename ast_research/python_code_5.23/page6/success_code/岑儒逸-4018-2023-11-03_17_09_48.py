def shift(lst):
    lst=list(lst)
    a=lst[-1]
    lst.remove(a)
    ls1=[a]+lst
    return ls1
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

