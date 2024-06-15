lst = eval(input())
ans = sum(lst) / len(lst)
if ans - int(ans) == 0:
    print(ans)
else:
    print("%.2f"%ans)

