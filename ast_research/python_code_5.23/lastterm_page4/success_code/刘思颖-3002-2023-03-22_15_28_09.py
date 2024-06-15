lst = eval(input())
a = sum(lst)
b = a/len(lst)
c = round(b)
if b%c==0:
    print(c)
else:
    print("%.2f"%(b))
