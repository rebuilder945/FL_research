def shift(lst):
    lst2 = []
    lst2.append(list1[len(list1)-1])
    for i in range(len(list1)-1):
        j = i+1
        lst2.append(list1[j])
    list1 = lst2

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

