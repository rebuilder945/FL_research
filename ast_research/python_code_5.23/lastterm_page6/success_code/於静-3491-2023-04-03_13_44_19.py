def shift(lst):
    lst.insert(0,lst.pop())#于零位插入用pop函数删掉的最后一位
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

