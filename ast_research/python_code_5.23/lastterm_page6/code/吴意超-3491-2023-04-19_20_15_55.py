def shift(lst):
n = len(list(list1))
    list1 = []
    for i in range(n):
        m = list1.remove(-1)
        list1.append(m)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

