#输入一个由字符串构成的列表和两个整数n和m（n和m在输入列表的下标范围以内），交换其中两个元素的值，打印输出交换后的列表。li
list1 = input().split()   #如果用split(""), ""里面别忘了敲一个空格啊
n,m = input().split()   #如果里面是列表，外面不可以加eval了，eval里面必须是string
list1[int(n)],list1[int(m)] = list1[int(m)],list1[int(n)]             #注意你的操作是在原列表之外还是改变了原列表的值   #什么奇葩操作？怎么转成列表又解除列表，多麻烦阿
print(list1)
#直接a[n],a[m] = a[m],a[n]或者
