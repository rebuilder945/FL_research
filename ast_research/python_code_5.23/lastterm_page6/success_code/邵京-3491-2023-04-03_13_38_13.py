def shift(lst):
    b=[]
    b.append(lst[0])
    for i in range(1,len(lst)):
        b.append(lst[i])
    return(b)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

