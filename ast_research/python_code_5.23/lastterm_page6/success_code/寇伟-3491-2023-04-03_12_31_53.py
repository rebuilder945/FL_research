def shift(lst):
    ls=[]
    ls.append(lst[-1])
    for i in lst:
        if i!=lst[-1]:
            ls.append(i)
    lst = ls[:]
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

