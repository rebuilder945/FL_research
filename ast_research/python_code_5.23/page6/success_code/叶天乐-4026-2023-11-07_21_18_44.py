n = eval(input())
a,b,sum = 2,1,0
for i in range(n):
    sum = sum=a/b
    b,a = a,a+b
print("%.4f"%sum)
    
