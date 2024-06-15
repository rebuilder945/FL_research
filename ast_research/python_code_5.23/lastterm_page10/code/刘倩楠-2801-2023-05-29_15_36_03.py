a=input()
s=list(a)
m=0
for x in s:
    if x.isdigit():
        m+=1
    elif x.isupper():
        m+=1
    elif x.islower():
        m+=1
    elif len(s)>=8:
        m+=1
    elif x in "~!@#$%^&*()_=-/,.?<>;:[]{}|\":
        m+=1
print(m)
