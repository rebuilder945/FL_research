a = eval(input())
c = sum(a)%len(a)
d = sum(a)/len(a)
if c == 0:
    print(int(d))
else:
    print("%.2f"%(d))
        

