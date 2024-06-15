ls = eval(input())
ls.sort(reverse=True)
max = ''.join(str(i) for i in ls)
print(max)
