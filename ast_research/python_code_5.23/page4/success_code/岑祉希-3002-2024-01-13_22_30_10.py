lst = eval(input())
totol = 0
for i in lst:
    totol +=i
a = float(totol)/len(lst)
if totol % len(lst) == 0:
    print('%d'%a)
else:
    print("%.2f"%a)
