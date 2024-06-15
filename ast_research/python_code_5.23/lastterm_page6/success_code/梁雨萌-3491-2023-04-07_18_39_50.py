def shift(lst):
    a=lst.pop()
    lst.reverse()
    lst.append(a)
    lst.reverse()
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

