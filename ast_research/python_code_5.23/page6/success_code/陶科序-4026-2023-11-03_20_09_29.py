a = 2
b = 1
s = 0
n= eval(input())
for i in range (n):
    s +=a/b
    a,b = (a+b),a
print("%.4f"%s)
    
    
