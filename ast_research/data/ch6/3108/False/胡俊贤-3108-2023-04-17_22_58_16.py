ls=eval(input())
s='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    a=s[i]
    n=ls.count(a)
    print(a,end=',')
    print(n)
