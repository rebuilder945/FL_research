def shift(lst):
    length=len(lst)
    for i in range(length-1):
        lst.insert(0,lst.pop())
    


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

