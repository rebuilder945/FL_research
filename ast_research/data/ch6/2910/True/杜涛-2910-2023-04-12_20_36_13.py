h = eval(input())
N = eval(input())
a=[h,h]
for i in range(N-2):
    h=h/2
    a.append(h)
print("%.2f"%sum(a))
    
