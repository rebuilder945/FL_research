def main(s1):
    '判断星级'
    global mark
    for i in s1:
        if i.isdigit() and '1' not in mark:
            mark += ['1']
        if i >= 'a' and i <= 'b' and '2' not in mark:
            mark += ['2']
        if i >= 'A' and i <= 'B' and '3' not in mark:
            mark += ['3']
        if len(s) >= 8 and '4' not in mark:
            mark += ['4']
        if i in '~!@#$%^&*()_=-/,.?<>;:[]\}\}|\\' and '5' not in mark:
            mark += ['5']

mark = []
s = input()
#使\失效
s1 = r'{}'.format(s)
main(s1)
print(len(mark))
