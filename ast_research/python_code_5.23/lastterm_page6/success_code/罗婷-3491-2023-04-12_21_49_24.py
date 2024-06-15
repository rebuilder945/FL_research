def shift(lst):
    m=lst[-1]
    m=[m]
    del lst[-1]
    lst=m+lst
    


       


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

