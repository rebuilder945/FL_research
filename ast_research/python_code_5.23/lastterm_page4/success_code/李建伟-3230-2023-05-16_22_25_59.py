lst = eval(input())
lst.sort(reverse=True)
s = ''
for i in lst:
    i = str(i)
    s = s+i
print(s)

