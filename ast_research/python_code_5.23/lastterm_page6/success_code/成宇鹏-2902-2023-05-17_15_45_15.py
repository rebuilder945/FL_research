# 有一个分数数列：2/1,3/2,5/3,8/5,13/8,21/13,...,从键盘输入一个正整数n，求出这个数列的前n项之和。
# def Fibonacci(num,n):
#     a = 0
#     while a <= n-1:
#         b = num[a+1] + num[a]
#         num.append(b)
#         a += 1
#     return num[n-1]
# num  =  [1,  2]
# n  =  int(input())
# print(Fibonacci(num,  n))

num = [1,2]
n = int(input())
a = 0
while a<=n-1:
    b = num[a]+num[a+1]
    num.append(b)
    a += 1
lst =[]
for x in range(n):
    c = num[x+1]/num[x]
    lst.append(c)
d = sum(lst)
print("%.4f"%d)

