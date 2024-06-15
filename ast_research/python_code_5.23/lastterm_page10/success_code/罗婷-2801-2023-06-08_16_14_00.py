psw=input()
power=[0,0,0,0,0]
for x in psw:
    if '0'<=x<='9':
        power[0]=1
    if 'a'<=x<='z':
        power[1]=1
    if 'A'<=x<='Z':
        power[2]=1
    if x in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\":
        power[3]=1
if len(psw)>=8:
    power[4]=1
print(power.count(1))
