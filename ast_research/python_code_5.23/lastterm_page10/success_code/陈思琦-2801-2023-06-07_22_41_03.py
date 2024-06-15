a=input()
power=[0,0,0,0,0]
for i in a:
    if '0'<=i<='9':
        power[0]=1
    if 'a'<=i<='z':
        power[1]=1
    if 'A'<=i<='Z':
        power[2]=1
    if i in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\":
        power[4]=1
if len(a)>=8:
    power[3]=1
print(power.count(1))
