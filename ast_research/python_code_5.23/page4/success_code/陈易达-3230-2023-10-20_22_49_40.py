ls = eval(input())
ls2 = ls.sorted(reverse=True)
result = int(''.join(map(str,ls2)))
print(result)
