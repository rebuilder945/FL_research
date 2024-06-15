lst = eval(input())
lst.sort()
print(lst)
m = ''
for i in lst[::-1]:
    m+=str(i)
print(m)
