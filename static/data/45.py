a = eval(input())
n, m = eval(input())
#eval函数用于将字符串转换为有效的Python表达式，但是如果输入的字符串格式不正确，就会导致SyntaxError
a[n], a[m] = a[m], a[n]
print(a)