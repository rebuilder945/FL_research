ls=eval(input())
a=ls.count(0)
for i in ls:
    if i==0:
        ls.remove(0)
lt=[0]
ii=lt*a
z=ls+ii
z.remove(0)#为啥
print(z)

