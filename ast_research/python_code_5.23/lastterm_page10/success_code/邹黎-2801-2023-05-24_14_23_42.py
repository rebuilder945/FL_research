a=input()
qd=0
for x in a:
    if x in "0123456789":
        qd+=1
        break
for x in a:
    if "a"<=x<="z":
        qd+=1
        break
for x in a:
    if "A"<=x<="Z":
        qd+=1
        break

if  len(a)>=8:
        qd+=1
        
for x in a:
    if x in "~!@#$%^&*()_=-/,.?<>;:{[]}|\\":
        qd+=1
        break
print(qd)
