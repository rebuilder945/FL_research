l=eval(input())
a=min(l)
b=max(l)
while True :   
    if a in l:
        l.remove(a)
    elif b in l:
        l.remove(b)
    else:
        break
print(l)
