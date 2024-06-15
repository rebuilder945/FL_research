def shift(lst):
    for x in range(len(lst)-1):
        lst.append(lst[0])
        del lst[0]
       

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

