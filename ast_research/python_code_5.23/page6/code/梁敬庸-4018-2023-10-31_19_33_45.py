def shift(lst):
    def shift(lst):
    lst2=lst.copy()
    del lst[0]
    lst.append(lst2[0])
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

