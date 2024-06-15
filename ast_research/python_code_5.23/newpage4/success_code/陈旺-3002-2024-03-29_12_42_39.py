# a=input()
# a=a.strip("[")
# a=a.rstrip("]")
# b=[int(i) for i in a.split(",")]
# c=[]
# for i in b:
#     if i<2:
#        c.append(i)
#     elif i==2:
#        None
#     else:
#        for x in range(2,i):
#           if i%x==0:
#              c.append(i)
# for i in b:
#    if i in c:
#       b.remove(i)
# print(b)
a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[int(i) for i in a.split(",")]
for i in b:
    ls = list()  # 定义一个列表
    for j in range(2, i):  # 输入数字范围
      count = 0
      for i in range(1, j + 1):  # 这里范围是从 1 到 该数本身
          if (j % i == 0):  # 如果只有1和本身能除尽计数2次
              count += 1
      if (count == 2):  # 再判断若2个因数就是素数，否则不是
          ls.append(j)
print(ls)

