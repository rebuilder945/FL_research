#输入三个正整数n，m，l，生成指定长度的等差数列，存入列表中。其中n表示起始值，m表示列表元素的数量，l表示公差。
n,m,l = int(input()),int(input()),int(input())
list = []
for i in range(m):
    list.append(n + i*l)
print(list)
#另一种方法：
# n,m,l = list(map(int,input().split(",")))或者n,m,l = input.split(",")或者n,m,l = int(input()),int(input()),int(input())
# ls = [n+i*l for i in range(m)]
# print(ls)
