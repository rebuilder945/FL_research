lst = eval(input())
lst.sort()
m = ''
for i in lst[::-1]:
    m+=str(i)
if m[0]=='0':
    print(0)
else:
    print(m)
