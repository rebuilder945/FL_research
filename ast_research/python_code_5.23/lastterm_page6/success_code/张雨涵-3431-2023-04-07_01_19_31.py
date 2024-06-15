t = eval(input())
a = 0
b=0
if 1<=t<=10:
    if t%2==0:
        a = 0
    else:
        a = 1
elif 11<=t<=18:
    if t%2==0:
        a = 1
    else:
        a = 0
elif 19<=t<=28:
    if t%2==0:
        a = 0
    else:
        a = 1
elif 29<=t<=36:
    if t%2==0:
        a = 0
    else:
        a = 1
elif t==0:
    a=2
else:
    a=3
if a==0:
    b = "black"
elif a == 1:
    b = "red"
elif a==2:
    b = "green"
else:
    b = "error"
print(b)
