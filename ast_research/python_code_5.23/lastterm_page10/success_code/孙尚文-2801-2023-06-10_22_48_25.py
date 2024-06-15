a=[0,0,0,0,0]
b=input()
for i in b:
    if i.isnumeric():
        a[0]=1
    elif 'a'<=i<="z":
        a[1]=1
    elif "A"<=i<='Z':
        a[2]=1
    if i in " ~!@#$%^&*()_=-/,.?<>;:[{]}|\ ":
        a[4]=1
    if len(b)>=8:
        a[3]=1
print(sum(a)) 
