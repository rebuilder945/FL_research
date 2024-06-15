def shift(lst):
     lll=[]
    for i in lst:
        if i == lst[0]:
            continue
        lll.append(i)
    lll.append(lst[0])
    return lll

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

