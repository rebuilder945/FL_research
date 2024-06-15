a = list(eval(input()))
c = sum(a) /len(a)
if sum(a) % len(a) == 0:
    print(int(c))
else:
    print("%.2f"%(c))
