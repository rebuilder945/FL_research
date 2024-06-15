def shift(lst):
    b=[]
    b.append(lst[len(lst)-1])
    for i in range(0,len(lst)-1):
        b.append(lst[i])
    lst[:]=b[:]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

