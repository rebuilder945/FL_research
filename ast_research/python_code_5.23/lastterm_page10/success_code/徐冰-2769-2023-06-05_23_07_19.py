l=input()
print(l)
n="abcdefghijklmnopqrstuvwxyz"
ls=[x for x in n]
for x in l:
    if x.isalpha():
        if x.isupper():
            x=x.lower()
            y=ls[25-ls.index(x)]
            print(y.upper(),end="")
        else:
            y=ls[25-ls.index(x)]
            print(y,end="")
    else:
        print(x,end="")
