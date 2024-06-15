n1 = eval(input())
s = sum(n1)/len(n1)
if s - int(s)==0:
    print(int(s))
else:
    print("%.2f"%s)
