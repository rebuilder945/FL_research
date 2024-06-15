ls = eval(input())
ls.sort(reverse=True)
ls = [str(i) for i in ls]
x = ''.join(ls)
if len(x) > 1:
    x = 0
print(x)
