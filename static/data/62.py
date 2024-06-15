ls = eval(input())
n = eval(input())

ls2 = ls * n
ls3 = [x * x for x in ls2]

ls4 = []
for x in ls3:
    a = ord(str(x))
    #想要对整数进行平方操作，并将结果转换为字符，您可以先将整数转换为字符串，然后再进行操作。
    ls4.append(chr(a))

print(ls4)