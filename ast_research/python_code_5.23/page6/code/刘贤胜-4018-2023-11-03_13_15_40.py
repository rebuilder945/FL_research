def shift(lst):
list2=list1.copy
list1[0]=list2[-1]
list1[-1]=list2[0]
    return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

