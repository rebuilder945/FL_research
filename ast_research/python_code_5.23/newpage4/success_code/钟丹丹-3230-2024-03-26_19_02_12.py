n = eval(input())
n.sort(reverse=True)
m=""
for x in n:
    m=m + str(x)
if m[0] in ['0']:
    print("0")
else:
    print(m)
