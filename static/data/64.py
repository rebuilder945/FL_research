ls1 = input()
n, m = eval(input())
#想要删除字符串中的某个范围的字符，可以将字符串转换为列表进行操作，然后再将其转换回字符串。
#首先将输入的字符串 ls1 转换为列表，然后执行删除操作，最后将列表转换回字符串。
if str(n) in ls1 and str(m) in ls1:
    n = int(n)
    m = int(m)
    if n < m:
        ls1 = list(ls1)
        del ls1[n:m]
        ls1 = ''.join(ls1)
        print(ls1)
    else:
        ls1 = list(ls1)
        del ls1[m:n]
        ls1 = ''.join(ls1)
        print(ls1)
else:
    print("error")