# 输入一个自然数列表，找出只出现一次的元素，并升序输出。如果没有只出现一次的元素，则输出False。
lst = eval(input())
lst1 = []
for x in lst:
    if lst.count(x) == 1:
        lst1.append(x)
if len(lst1) != 0:
    lst1.sort()
    print(lst1)
else:
    print(False)
