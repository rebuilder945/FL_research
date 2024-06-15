list = list(eval(input()))
n,m = eval(input())
i = 1
a = list[n]
while i <= m:
    list.append(a)
    i += 1
print(list)

