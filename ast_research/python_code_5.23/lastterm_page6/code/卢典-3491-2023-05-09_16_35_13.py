def shift(lst):
if len(lst) == 0:
        return lst
    else:
        last_element = lst.pop()
        lst.insert(0, last_element)
        return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

