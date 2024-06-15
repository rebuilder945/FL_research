def shift(lst):
    # a=copy.deepcopy(lst)
    # b=copy.deepcopy(lst)
    # a=list(a[-1])
    # b=b[0:-1]
    # print(a)
    # print(b)
    # lst=a+b   为什么错
    lst.insert(0,lst.pop())

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

