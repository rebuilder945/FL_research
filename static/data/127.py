n, m = map(int, input().split(' '))
ls = []

if type(n) != int or type(m) != int or n < 0 or n >= 10:
    ls = [ls]
else:
    for a in range(n, m):
        sa = str(a)
        for b in range(n, m):
            sb = str(b)
            for c in range(n, m):
                sc = str(c)
                sabc = sa + sb + sc
                if int(sa) != 0 and sa != sb and sb != sc and sc != sa and len(sabc) == 3 and sabc not in ls:
                    ls.append(sabc)

if ls == []:
    print("illegal input")
else:
    print("".join(ls))

#处理输入时，将 ls 初始化为一个空列表 []，
#然后在一些情况下，将其重新赋值为包含一个空列表的列表 ls=[ls]，
#这样做会导致 ls 变成了一个包含一个空列表的列表，而不是包含字符串的列表。