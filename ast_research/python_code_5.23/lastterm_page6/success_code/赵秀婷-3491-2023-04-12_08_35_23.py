def shift(lst):
    n = len(lst)
    k = k % n
    if k == 0:
        return lst
    for i in range(k):
        lst.insert(0, lst.pop())
    return lst
       


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

