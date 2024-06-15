boy, girl = eval(input())
bs = boy / (boy + girl)
gs = girl / (boy + girl)
s = "The male students ratio is %.2f%%, the female students ratio is %.2f%%" % (bs * 100, gs * 100)
print(s)
#代码中存在一些语法错误，导致字符串格式化出现了问题