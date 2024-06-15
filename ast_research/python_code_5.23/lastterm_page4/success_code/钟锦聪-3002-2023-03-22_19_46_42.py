a = eval(input())
b = sum(a)/len(a)
c = "%.2f"%(b)
d = c[-2::]
e= c[-4::-1]
if d == "00":
    print(e)
else:
    print(c)

