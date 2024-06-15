i = eval(input())
n = {}

for a in i:
    if a in n:
        n[a] += 1
    else:
        n[a] = 1
##不能直接在变量名后面调用函数来增加变量的值，需要使用赋值语句或者递增运算符（例如 +=）来修改变量的值
for a in n:
    if n[a] == 1:
        print(a, end="")

if not any(n[a] == 1 for a in n):
    print("false")