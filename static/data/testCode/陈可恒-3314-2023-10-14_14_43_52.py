ruler = eval(input())
acre = ruler/43560
a = round(acre,3)
print("The land area is {%.2f}".format(a))
# 只是你想输出的时候，永远是考虑字符串格式化
# 而不是使用round
# 计算才考虑round


