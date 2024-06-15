b=[]
while True:
    a=input()
    if a=='#':
        print(len(b),sum(b))
        break
    else:
        b.append(eval(a))




