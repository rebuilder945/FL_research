lst = eval(input())
#lst = list(lst)
n = sum(lst)
if n % len(lst)==0:
    a = n / len(lst)
    print("%.d"%a)
else:
    b = n / len(lst)
    print("%.2f"%b)
