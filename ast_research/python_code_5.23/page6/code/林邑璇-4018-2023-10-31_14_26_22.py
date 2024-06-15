def shift(lst):
    a＝len（lst）
    for i in range（a）:
        lst[a－i－1],lst[a－i－2]＝lst[a－i－2],lst[a－i－1]
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

