# 月份对应的季节
# 【问题描述】
# 根据用户输入的月份，打印该月份所属的季节，如果输入的数据不在1~12范围内，输出“error" 
# 提示：3，4，5 spring ；6，7，8 summer ；9，10，11 autumn ；12，1，2 winter
n = eval(input())
if n >= 3 and n <= 5:
    print('spring')
elif n >= 6 and n <= 8:
    print('summer')
elif n >= 9 and n <= 11:
    print('autumn')
elif n == 12 or n == 1 or n == 2:
    print('winter')
else:
    print('error')
