ls = eval(input())
ls.sort(reverse=True)
ls = [str(i) for i in ls]
x = ''.join(ls)
print(x)
