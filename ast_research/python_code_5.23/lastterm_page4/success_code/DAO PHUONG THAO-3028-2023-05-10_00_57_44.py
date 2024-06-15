n,m,l=map(int,input().split(',')) # 输入n、m、l，转换为正数类型并存储到变量中
lst=[] # 定义一个空列表用于存储等差数列
for i in range(m):  #range 函数也是不包括右端数字的
    lst.append(n+i*l) #计算等差数列每个元素的值，并添加到lst中

print(lst)
