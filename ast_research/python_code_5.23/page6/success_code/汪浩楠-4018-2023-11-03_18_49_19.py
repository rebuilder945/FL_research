def shift(lst):
    a=[i for i in range (len(lst))]
    b=a.pop()
    a.append(b)


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

