s=input()
x=[0,0,0,0,0]
for m in s:
    if m.isdigit():
        x[0]=1
    if m.isalpha():
        if m.islower():
            x[1]=1
        if m.isupper():
            x[2]=1
    if len(s)>=8:
        x[3]=1
    if m in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\":
        x[4]=1
print(x.count(1))
