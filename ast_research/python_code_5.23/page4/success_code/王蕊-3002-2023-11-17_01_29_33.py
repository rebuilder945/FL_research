lst = eval(input())
n = sum(lst)/len(lst)
Ave = int(n)
if n > Ave:
    print("%.2f"%(n))
else:
    print(Ave)
