n = eval(input())
ls = []
for x in str(n):
    x = int(x)+5
    x = x%10
    ls.append(x)
ls[0],ls[-1] = ls[-1],ls[0]
ls[1],ls[-2] = ls[-2],ls[1]
result = int("".join(map(str,ls)))
print(result)
