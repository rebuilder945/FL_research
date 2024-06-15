n=eval(input())
x=2+3+5+8
y=1+2+3
a=0
for i in range(n-3):
    y=y+i+2**i-1
    x=x+i+2**i-1
    a=a+x/y
print(a)

