def shift(lst):
    lll=lst.copy()
    lst.clear()
    lst.append(lll[-1])
    a=len(lll)
    for i in range(a-1):
        lst.append(lll[i])

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

