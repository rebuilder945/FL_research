def shift(lst):
    m = list(lst[-1])
    k = list(lst[0])
    l = lst[1:-1]
    listx = m+k+l
    lst.clear
    for i in listx:
        lst.append(i)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

