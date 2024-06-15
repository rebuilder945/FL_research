def shift(lst):
    b = lst.pop()
    lst.reverse()
    lst.append(b)
    lst.reverse()


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

