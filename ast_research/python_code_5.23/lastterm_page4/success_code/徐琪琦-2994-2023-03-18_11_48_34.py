#输入一个整数列表和整数n(n可以是负数）和正整数m，从该列表中选择第n个元素(指序号为n，而不是我们通常认为的“第n个”），把该元素重复m次，然后放到列表的尾端，最后输出列表。如果输入的n值不在列表下标范围之内，则输出"error"
list1 = list(eval(input()))     #实际上一开始输入的也不是列表,是元组，你不可以用split把元组变成列表，得用list
n,m = eval(input())
if len(list1) > 1:                   #居然可以这样写啊0 < n < len(list1)，不需要and连接
    a = list1[n]
    for i in range(m):
        list1.append(a)
        i += 1
    print(list1)
elif len(list1) == 1:
    if n == 0 or n == -1:
        a = list1[0]
        for i in range(m):
            list1.append(a)
            i += 1
        print(list1)
    else:
        print("error")
else:
    print("error")


