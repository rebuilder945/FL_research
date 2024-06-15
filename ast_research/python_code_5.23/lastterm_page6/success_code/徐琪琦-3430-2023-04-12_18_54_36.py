#根据用户输入的月份，打印该月份所属的季节，如果输入的数据不在1~12范围内，输出“error" 
#提示：3，4，5 spring ；6，7，8 summer ；9，10，11 autumn ；12，1，2 winter
month = eval(input())
if month < 1 or month > 12:
    print("error")
elif 3 <= month <= 5:
    print("spring")
elif 6 <= month <= 8:
    print("summer")
elif 9 <= month <= 11:
    print("autumn")
else:
    print("winter")

