x = '1,2,3'
#错误写法：a,b = eval(x), a,b,c,d = eval(x)
a,b,c = eval(x)
print(a,b,c)