'''a=eval(input())
a.sort()
a.reverse()
s=''
for x in a:
    s=s+str(x)
s=int(s)
print(s)'''

a=eval(input())
a.sort()
a.reverse()
print(int(''.join(map(str,a))))
