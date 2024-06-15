"""【问题描述】
根据用户输入的月份，打印该月份所属的季节，如果输入的数据不在1~12范围内，输出“error" 
提示：3，4，5 spring ；6，7，8 summer ；9，10，11 autumn ；12，1，2 winter
【输入形式】
月份（整数）
【输出形式】
spring or summer or autumn or winter or error
【样例输入】
3
【样例输出】
spring"""
sea = "springsummerautumnwinter"
n= eval(input())
a=(n-3)//3
if n==1 or n==2:
    print("winter")
if type(n)!=int or n<=0 or n>=12:
    print("error")
else:
    print(sea[6*a:6*a+6])
