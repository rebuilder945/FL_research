a=eval(input())
a.sort(reverse=True)
s = ''
for i in a:
    s += str(i)
print(int(s))
