a=input()
p=[0,0,0,0,0]
for x in a:
    if "0"<=x<="9":
        p[0]+=1
    if "a"<=x<="z":
        p[1]+=1
    if "A"<=x<="Z":
        p[2]+=1
    if len(a)>=8:
        p[3]+=1
    if x in "~!@#$%^&*()_=-/,.?<>;:[]\{\}|\\":
        p[4]+=1
print(5-p.count(0))

    
