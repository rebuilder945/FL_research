a=eval(input())
b=''
while len(a)>0:
    c=max(a)
    b+=str(c)
    a.remove(c)
if b[0]==0:
    print("0")
else:print(b)
