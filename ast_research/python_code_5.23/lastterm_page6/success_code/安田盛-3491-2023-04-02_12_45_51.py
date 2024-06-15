def shift(lst):

    for x in range(len(list1),0,-1):
        a=list1.pop(x-1)
        list1.insert(x,a)
    return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

