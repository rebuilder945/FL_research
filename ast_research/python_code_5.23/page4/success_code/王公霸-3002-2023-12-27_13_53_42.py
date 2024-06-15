lista= eval(input())
x = len(lista)
s = sum(lista)
t = s/x
a = int(t)
if t%a==0:
    print(a)
else:
    print(f"{t:.2f}")

