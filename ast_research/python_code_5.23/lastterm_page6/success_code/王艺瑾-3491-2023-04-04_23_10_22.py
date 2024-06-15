def shift(lst):
    list2=[]
    list2=copy.list1
    for i in range(len(list1)):
        list1[i]=list2[i+1]
    list1.insert(0,list2[0])
    return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

