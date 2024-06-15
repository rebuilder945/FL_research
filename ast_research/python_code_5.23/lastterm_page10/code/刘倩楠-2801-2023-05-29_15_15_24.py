a=input()
s=list(a)
n=list(~!@#$%^&*()_=-/,.?<>;:[]{}|\)
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
    elif for i in n in s:
        m+=1
print(m)
