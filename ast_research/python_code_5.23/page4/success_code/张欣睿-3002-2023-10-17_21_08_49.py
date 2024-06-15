a = eval(input())
b = sum(a)
c = b/len(a)
if c == int(c):
    print("%d"%(c))
else:
    print("%.2f"%(c))


