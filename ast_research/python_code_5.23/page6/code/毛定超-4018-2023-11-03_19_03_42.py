def shift(lst):
 m=list1[0]
    del(list1[0])
    list1.append(m)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

