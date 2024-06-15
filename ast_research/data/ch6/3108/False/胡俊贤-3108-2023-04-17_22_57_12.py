ls=eval(input())
s='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    a=s[i]
    n=ls.count(i)
    print(a,end=',')
    print(n)
