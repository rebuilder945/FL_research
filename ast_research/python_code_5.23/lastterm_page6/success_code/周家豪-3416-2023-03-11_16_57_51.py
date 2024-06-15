# 示例：输入212F      输出100.00C
#      输入100c      输出212.00F
#       输入不符合格式要求，输出“Error”     

# TempStr = input()
# if TempStr[-1] in ['F','f']:
#     C = (eval(TempStr[0:-1]) - 32)/1.8
#     print("%.2fC"%(C))
# elif TempStr[-1] in ['C','c']:
#     F = 1.8*eval(TempStr[0:-1]) + 32
#     print("%.2fF"%(F)
# else:
#     print("Error")

money=input()
if money[0] in ['$']:
    yuan=(eval(money[1:])*6.78)
    print("&%.2f"%yuan)
elif money[0] in ['&']:
    dollar=(eval(money[1:])/6.78)
    print("$%.2f"%dollar)
elif money[0:3] in ["USD"]:
    yuan=((eval(money[3:])*6.78))
    print("RMB%.2f"%yuan)
elif money[0:3] in ["RMB"]:
    dollar=((eval(money[3:])/6.78))
    print("USD%.2f"%dollar)
else:
    print("Error")

# print (money[0:3],type(money[0:3]))
