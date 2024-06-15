# 【问题描述】

# 在一个赌博用的转盘上，口袋的编号是从0到36，口袋的颜色如下： 

#     从1号袋到10号袋，奇数的口袋是红色，偶数的口袋是黑色。

#     从11号袋到18号袋，奇数的口袋是黑色，偶数的口袋是红色。

#     从19号袋到28号袋，奇数的口袋是红色，偶数的口袋是黑色。 

#     从29号袋到36号袋，奇数的口袋是黑色，偶数的口袋是红色。

#     0号口袋是绿色

# 请编写一个程序，根据用户输入的口袋编号，输出口袋的颜色。 如果用户输入的数字不在0~36这个范围内，则输出“error”。

# 【输入形式】
# 整数

# 【输出形式】

# green or red or black or error
# 【样例输入1】

# 0
# 【样例输出1】

# green

# 【样例输入2】

# 11
# 【样例输出2】

# black

ls=list(range(0,37))
n=int(input())
if not n in ls:
    print("error")
elif n==0:
    print("green")
elif n%2!=0:
    if n>=1 and n<=10:
        print("red")
    elif n>=11 and n<=18:
        print("black")
    elif n>=19 and n<=28:
        print("red")
    elif n>=29 and n<=36:
        print("black")
elif n%2==0:
    if n>=1 and n<=10:
        print("black")
    elif n>=11 and n<=18:
        print("red")
    elif n>=19 and n<=28:
        print("black")
    elif n>=29 and n<=36:
        print("red")


