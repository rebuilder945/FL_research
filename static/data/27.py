# 使用一个input（）即可，输入多个值1,2进行拆分
#错误写法：a,b = eval(input()，input())
a,b = eval(input())
y = int(a) + int(b)
print(y)