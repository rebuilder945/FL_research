s=input()
a=[0,0,0,0,0]
for i in s:
    if "0"<=i<="9":
        a[0]=1
    elif "a"<=i<="z":
        a[1]=1
    elif "A"<=i<="Z":
        a[2]=1
    elif i in "~!@#$%^&*()_=-/,.?<>;:[]{\}|\\":
        a[4]=1
if len(s)>=8:
    a[3]=1
    
print(sum(a))
