def shift(lst):
    a=lst[-1]
    lst2=[]
    lst2.append(a)
    for i in range(len(lst)-1):
        lst2.append(lst[i])

    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

