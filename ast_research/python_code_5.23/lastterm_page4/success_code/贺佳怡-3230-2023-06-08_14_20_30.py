a=eval(input())
b=len(a)
evn=0
while b>0:
    evn+=mac(a)*b
    b-=1
    a.remove(max(a))
print(evn)

