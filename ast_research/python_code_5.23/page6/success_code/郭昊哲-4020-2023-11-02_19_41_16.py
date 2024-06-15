h=eval(input())
n=eval(input())
x=h
for i in range(n):
    if i==1:
        pass
    if i>0:
        x+=h/2/i
print("{:.2f}".format(x))


