# 【问题描述】从键盘输入两个整数n和m（要求n<m），编程求出由n到m(不包含m)中的整数组合而成的所有不含重复数字的三位数。若n和m的输入不合法或者没有符合条件的三位数则提示输出“illegal input"。

# 【输入形式】输入一行，内容为两个以空格分隔的整数，分别表示n和m。

# 【输出形式】以空格分隔输出所有符合条件的三位数。

# 【样例输入】1 4

# 【样例输出】123 132 213 231 312 321

# 【样例输入】2 4

# 【样例输出】illegal input

# 【样例输入】0 3

# 【样例输出】102 120 201 210

n,m=map(int,input().split())
if n>m or m-n<3 or n<0 or m<0 or n>9 or m>9:
    print("illegal input")
else:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and j!=k and i!=k:
                    print(str(i)+str(j)+str(k),end=" ")
