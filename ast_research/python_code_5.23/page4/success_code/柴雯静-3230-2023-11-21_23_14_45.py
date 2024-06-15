a = eval(input())
a.sort(reverse=True)
s=''
for x in a:
    s = s+str(x)
s = int(s)
print(s)
