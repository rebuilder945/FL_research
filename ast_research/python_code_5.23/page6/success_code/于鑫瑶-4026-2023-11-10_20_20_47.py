n=eval(input())
x=5
y=3
a=2/1+3/2+5/3
for i in range(n-3):
    y=y+i+2**(i+1)-1
    x=x+y
    a=a+x/y
print(a)

