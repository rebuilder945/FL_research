def shift(lst):
    a = len(lst)-1
    for i in range(a) :
        lst [i+1] = lst [i]
        lst[0] = lst[-1]
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

