a=eval(input())
b=eval(input())
c=[a]
for i in range(1,b):
    c=c+[a*(0.5**i)]*2
print("%.2f"%sum(c))

