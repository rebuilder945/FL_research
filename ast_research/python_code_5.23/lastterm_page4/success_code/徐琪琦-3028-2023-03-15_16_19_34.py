#输入三个正整数n，m，l，生成指定长度的等差数列，存入列表中。其中n表示起始值，m表示列表元素的数量，l表示公差。
n,m,l = eval(input())
list = []
for i in range(m):
    list.append(n + i*l)
print(list)
