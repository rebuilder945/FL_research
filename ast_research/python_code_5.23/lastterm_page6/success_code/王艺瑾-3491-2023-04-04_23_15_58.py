def shift(lst):
    list2=[]
    list2=list1.copy()
    for i in range(len(list1)):
        list1[i]=list2[i-1]

    return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

