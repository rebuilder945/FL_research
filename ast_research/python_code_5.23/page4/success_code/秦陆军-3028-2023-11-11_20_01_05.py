#【问题描述】
#输入三个正整数n，m，l，生成指定长度的等差数列，存入列表中。其中n表示起始值，m表示列表元素的数量，l表示公差。
#【输入形式】
#在同一行输入n，m，l三个值，中间用英文逗号分隔。
#【输出形式】
#打印输出列表
n,m,l = eval(input())
lst = []
lst.append(n)
while len(lst) < m:
  s = lst[-1]+l
  lst.append(s)
print(lst)
