ls = eval(input())
ls.sort(reverse=True)
ls = [str(i) for i in ls]
x = ''.join(ls)
if "00" in x:
    x = 0
print(x)
