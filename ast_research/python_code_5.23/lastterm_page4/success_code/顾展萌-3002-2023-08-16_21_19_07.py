lst1 = eval(input())
m = 0
q = len(lst)
for i in lst1:
    m += i
n = m/q
if m%q == 0:
    print("%d"%n)
else:
    print("%.2f"%n)



    












