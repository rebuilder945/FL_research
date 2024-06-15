a=input()
m=[0,0,0,0,0]
n="~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
if len(a)>=8:
    m[0]=1
for x in a[:]:
    if x.isdigit():
        m[1]=1
    elif x.isupper():
        m[2]=1
    elif x.islower():
        m[3]=1
    elif x in n:
        m[4]=1
print(sum(m))
