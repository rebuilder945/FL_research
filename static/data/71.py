list1 = eval(input())
list2 = sorted(list1)

while len(list1) > 0 and max(list1) == max(list2):
    list1.remove(max(list1))

while len(list1) > 0 and min(list1) == min(list2):
    list1.remove(min(list1))
#在每次迭代中都会修改 list1，导致 list1 可能会变为空列表，从而导致 max() 或 min() 函数无法找到最大值或最小值。
#在 while 循环中添加了对 list1 的长度是否大于 0 的检查，以避免出现空列表的情况。
print(list1)