def shift(lst):
    a=ls[-1]
    for i in range(len(ls)):
        ls1[i+1]=ls[i]
        ls1[0]=a
    return list(ls1)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

