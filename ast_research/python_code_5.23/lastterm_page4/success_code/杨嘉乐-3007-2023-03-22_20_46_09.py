l=eval(input())
n,m=eval(input())
a=0
if n>len(l) or m>len(l):
    print("error:")
    a=1
for i in range(m-n):
    l.pop(n+i)
if a==0:
    print(l)


