lst = eval(input())
lst.sort(reverse = True)
ans = 0
for x in lst:
    ans = ans * 10 + x
print(ans)


