lsR = eval(input())
n = sum(lsR)/len(lsR)
if n.is_integer():
    print(int(n))
else:
    print(f"{n:.2f}")




