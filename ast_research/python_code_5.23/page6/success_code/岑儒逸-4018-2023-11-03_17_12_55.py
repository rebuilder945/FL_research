def shift(lst):
    lst=list(lst)
    ls1=[lst[-1]]
    lst.remove(lst[-1])
    for i in range(0,len(lst)-1):
        ls1=ls1+[lst[i]]
    return ls1
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

