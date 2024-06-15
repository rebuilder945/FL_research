#读入一个列表lst和正整数n和m，然后删除n~m之间的元素，不包括m位置的元素，其中n小于或者等于m。
# 如果输入的n和m不在列表lst的下标范围内，则输出"error"。
lst = eval(input())
n,m = input().split(",")
n = int(n)
m = int(m)
if n > len(lst):
    print("error")
else:
    if n < m:
        del lst[n:m]
    else:
        del lst[n]
print(lst)
