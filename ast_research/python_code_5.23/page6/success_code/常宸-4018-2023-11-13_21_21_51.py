def shift(lst):
    a = lst.pop(-1)
    lst.remove(-1)
    lst.append(-1)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

