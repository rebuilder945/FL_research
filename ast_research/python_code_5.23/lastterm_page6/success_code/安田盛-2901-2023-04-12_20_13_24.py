b=[]
while True:
    a=input()
    if a=='#':
        break
    else:
        b.append(int(a))
if b==[]:
    print(0,0)
else:
    print(len(b),sum(b))






