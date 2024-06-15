ls1 = input()
n, m = eval(input())

#在Python中，字符串是不可变的，无法直接对字符串进行删除操作。
#想要删除字符串中的某个范围的字符，可以通过切片的方式来实现。

if n < len(ls1):
    if m < len(ls1) and n < m:
        ls1 = ls1[:n] + ls1[m:]
        print(ls1)
    elif m < len(ls1) and n > m:
        ls1 = ls1[:m] + ls1[n:]
        print(ls1)
    else:
        print("error")
else:
    print("error")