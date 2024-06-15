str=input().split(' ')
n,m=input().split(' ')
n=int(n)#int函数只能表示一个字符而不能表示列表
m=int(m)
temp=str[m]#交换时的第三个临时变量，设置中间变量保存str【m】
str[m]=str[n]#str表示字符串
str[n]=temp#即为赋值交换
print(str)

