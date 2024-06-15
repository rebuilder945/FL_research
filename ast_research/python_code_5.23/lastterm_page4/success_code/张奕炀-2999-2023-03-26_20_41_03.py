list1 = input().split(' ')
a,b = input().split()               #空格输入多个元素的分别赋值
a = int(a)
b = int(b)
list1[a],list1[b] = list1[b],list1[a]
print(list1)
