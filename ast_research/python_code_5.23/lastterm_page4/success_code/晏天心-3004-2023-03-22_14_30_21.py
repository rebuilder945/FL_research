# 输入一个正整数n，输出前n个既是回文又是素数的数，要求每行输出10个数并以空格隔开
# 回文素数：一种既是回文数又是素数的数字
# “回文数“是指正读反读都一样的数字，
# 素数指在大于1的自然数中，除了1和它本身以外不再有其它因数的自然数

# x = eval(input())
# def sushu(n):
#     for i in range(2,n//2+1):
#         if n % i == 0:
#             return False
#     return True
# def huiwenshu(n):
#     if str(n) == str(n)[::-1]:
#         return True
#     else:
#         return False
# n = 40000
# lst = []
# for i in range(2,n):
#     if sushu(i) and huiwenshu(i):
#         lst.append(i)
# y = 0
# lst1 = []
# while y < x:
#     lst1.append(lst[y])
#     y += 1
# m = x//10
# if m == 0:
#     print(" ".join(str(i) for i in lst1))
# else:
#     z = 0
#     while z < m:
#         lst2 = lst1[10*z:10*z+10]
#         z += 1
#         print(str.format('{0:6}{1:6}{2:6}{3:6}{4:6}{5:6}{6:6}{7:6}{8:6}{9:6}',lst2[0],lst2[1],lst2[2],lst2[3],lst2[4],lst2[5],lst2[6],lst2[7],lst2[8],lst2[9]))
    # l = 0 - x%10
    # lst3 = lst1[l:]
    # print(" ".join(str(i) for i in lst3))
# print(" ".join(str(i) for i in lst1))

import math
def sushu(n):
    for i in range(2,int(math.sqrt(n))+1):#range(2,int(n**0.5//1)+1)也可以，而且不用导入数学模块，即import math不需要
        if n % i == 0:
            return False
    return True
def huiwenshu(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = eval(input())
count = 0
num = 2
ls = []
while count < n:
    if sushu(num) and huiwenshu(num):
        ls.append(num)
        count += 1
    num += 1
for i in range(len(ls)):
    if i % 10 != 0:
        print("{:6}".format(ls[i]),end="")
    else:
        print()
        print("{:6}".format(ls[i]),end="")

