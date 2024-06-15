def perman(a,b):
    c = a/(a+b)
    return c*100

m = eval(input())
n = eval(input())
male = perman(m,n)
female = perman(n,m)
print("The male students ratio is %.2f%%,the female students ratio is %.2f%%"%(male,female))
#%.2f%%是一种格式化字符串的写法，通常用于将一个浮点数值以百分比的形式输出。
# 其中，%.2f表示保留两位小数的浮点数，而%%表示输出一个百分号。
# 例如，如果一个浮点数值为0.5678，使用%.2f%%格式化后，输出结果为56.78%。
