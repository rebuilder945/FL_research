lst = eval(input())
a = sum(lst)
b = len(lst)
c = a/b
if a%b==0:
    print("%.d" %c)
else:
    print("%.2f" %c)
