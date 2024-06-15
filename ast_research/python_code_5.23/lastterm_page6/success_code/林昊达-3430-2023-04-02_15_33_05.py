# 【问题描述】

# 根据用户输入的月份，打印该月份所属的季节，如果输入的数据不在1~12范围内，输出“error" 

# 提示：3，4，5 spring ；6，7，8 summer ；9，10，11 autumn ；12，1，2 winter

# 【输入形式】

# 月份（整数）
# 【输出形式】

# spring or summer or autumn or winter or error

# 【样例输入】
# 3

# 【样例输出】
# spring

m=int(input())
if m==1 or m==2 or m==12:
    print("winter")
elif m==3 or m==4 or m==5:
    print("spring")
elif m==6 or m==7 or m==8:
    print("summer")
elif m==9 or m==10 or m==11:
    print("autumn")
else:
    print("error")
