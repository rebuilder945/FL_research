psw=input()
power=[0,0,0,0,0]
for i in psw:
    if "0"<=i<='9':
        power[0]=1
    if "a"<=i<="z":
        power[1]=1
    if "A"<=i<="Z":
        power[2]=1
    if i in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\":
        power[3]=1
if len(psw)>=8:
    power[4]=1
print(sum(power))
