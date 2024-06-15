def shift(lst):
    list2=[]
    list2.append(lst[-1])
    a=len(lst)-1
    for i in range(0,a):
        list2.append(lst[i])
    lst=list2
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

