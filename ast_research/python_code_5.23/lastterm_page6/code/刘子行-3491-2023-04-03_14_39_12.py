def shift(lst):
dick=list.pop(0)
    list.append(dick)
    return list

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

