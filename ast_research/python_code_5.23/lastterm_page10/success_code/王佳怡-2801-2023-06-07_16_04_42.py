a=input()
l=[0,0,0,0,0]
for i in a:
    if "0"<=i<="9":
        l[0]=1
    if "a"<=i<="z":
        l[1]=1
    if "A"<=i<="Z":
        l[2]=1
    if i in "~!@#$%^&*()_=-/,.?<>;:[]\{\}|\\":
        l[4]=1
if len(a)>=8:
        l[3]=1
print(l.count(1))
    
