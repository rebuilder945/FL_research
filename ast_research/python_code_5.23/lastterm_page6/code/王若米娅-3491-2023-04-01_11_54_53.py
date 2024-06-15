def shift(lst):
lst=eval(input())
    a=lst[-1]
    del lst[-1]
    lst.insert(0,a)
    return lst


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

