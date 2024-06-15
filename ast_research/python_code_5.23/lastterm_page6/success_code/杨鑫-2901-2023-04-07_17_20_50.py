all=0
n=""
b=0
f=True
while f:
    n=input()
    if n=="#":
        f=False
        print(b,all)
    else:
        all=all+eval(n)
        b=b+1
