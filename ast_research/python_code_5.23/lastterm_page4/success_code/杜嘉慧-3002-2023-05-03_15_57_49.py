lst = eval(input())
ans = sum(lst) / len(lst)
if ans - int(ans) == 0:
    print("%d"%ans)
else:
    print("%.2f"%ans)

