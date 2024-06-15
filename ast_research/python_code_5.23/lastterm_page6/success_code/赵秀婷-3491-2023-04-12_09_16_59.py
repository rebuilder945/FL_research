def shift(lst):
        a=lst[-1]
        del  lst[-1]
        lst.insert(0, a)  # 将数字添加到原列表的第一个位置
        return lst


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

