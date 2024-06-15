n, m = map(int, input().split())

s = ""
if n >= 0 and m - n >= 3:
    for a in range(n, m):
        for b in range(n, m):
            for c in range(n, m):
                if a != b and b != c and a != c:
                    if a != 0:
                        s += str(a) + str(b) + str(c) + " " + str(a) + str(c) + str(b) + " "
                    if b != 0:
                        s += str(b) + str(c) + str(a) + " " + str(b) + str(a) + str(c) + " "
                    if c != 0:
                        s += str(c) + str(a) + str(b) + " " + str(c) + str(b) + str(a) + " "
    print(s)
else:
    print("illegal input")
#将输入的内容解包给了三个变量 n, x, m，但实际上你只需要 n 和 m 来表示范围。因此，你应该只接收 n 和 m 两个值。