a=input()
b=input()
ls=list(a)
for i in ls:
    while i==b:
        ls.remove(i)
print(''.join(ls))
