#读入一个列表lst和正整数n和m，然后删除n~m之间的元素，不包括m位置的元素，其中n小于或者等于m。
# 如果输入的n和m不在列表lst的下标范围内，则输出"error"。
lst = eval(input())
n,m = eval(input())
if n < 0 or m < 0 or n > len(lst) - 1 or m > len(lst) - 1 :
    print("error") #是==而不是=！！！，而且<class 'int'>外面要加引号啊
else:
    del lst[n:m]
    print(lst)

