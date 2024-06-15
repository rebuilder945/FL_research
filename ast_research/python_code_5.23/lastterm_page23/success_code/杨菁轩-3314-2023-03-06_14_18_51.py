s=input()
a=eval(s.split(",")[0])
b=eval(s.split(",")[1])
c=eval(s.split(",")[2])
if a>=b:
    a=a
else:
    a=b
if a>=c:
    a=a
else:
    a=c
print(a)
