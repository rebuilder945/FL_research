n = eval(input())
ls = []
for x in str(n):
    x = int(x)+5
    x = x%10
    ls.append(x)
l = len(ls)
for i in range(l//2):
    ls[i],ls[l-i-1]=ls[l-i-1],ls[i]
r = int("".join(map(str,ls)))
print(r)

