s = 100
def a(arg):
    return arg*100
#错误写法：print("这是变量值%.f,这是函数返回值%.f"%(s,a))
print("这是变量值%.f,这是函数返回值%.f"%(s,a(s)))