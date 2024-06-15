lst = eval(input())
lst.sort()
m = ''
for i in lst[::-1]:
    m+=str(i)
print(m)
