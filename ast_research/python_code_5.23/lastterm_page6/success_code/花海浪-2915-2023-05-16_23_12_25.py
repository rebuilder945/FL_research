def shui(n):
    b=[]
    c=0
    for i in str(n):
        b.append(i)
    for i in b:
        c+=int(i)**3
    if c==n:
        return True
a=eval(input())
d=[]
for n in range(1,a+1):
    if shui(n) and n>100:
        d.append(n)
print(d)
if d==" ":
    print("None")
else:
    for i in d:
        print(i)


        




