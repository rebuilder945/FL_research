# 根据用户输入的月份，打印该月份所属的季节，如果输入的数据不在1~12范围内
# ，输出“error" 

# 提示：3，4，5 spring ；6，7，8 summer ；9，10，11 autumn ；12，1，2 winter
n = int(input())
if n ==4 or n ==5 or n ==3:
    print("spring")
elif n ==8 or n ==7 or n ==6:
    print("summer")
elif n ==11 or n ==10 or n ==9:
    print("autumn")
elif n ==12 or n ==1 or n ==2:
    print("winter")
else:
    print("error")
