lst = eval(input())
lst.sort(reverse=True)
res = ''.join(str(i) for i in lst)
print(res)

