a=input()
b=input()
ls=list(a)
ls2=list(b)
for i in ls:
    while i in ls2:
        ls.remove(i)
print(''.join(ls))
