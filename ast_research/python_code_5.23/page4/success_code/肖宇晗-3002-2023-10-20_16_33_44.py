l = eval(input())
t = len(l)
n = sum(l)
a = n/t
if type(a)==int:
    print(a)
elif type(a)==float:
    print("%.2f"%(a))
