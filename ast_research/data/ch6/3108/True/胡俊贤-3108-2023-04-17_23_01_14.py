ls=eval(input())
ls1=''.join(ls)
s='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    a=s[i]
    n=ls1.count(a)
    if n>0:
        print(a,end=',')
        print(n)
