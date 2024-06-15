psw=input()
power=[0,0,0,0]
for x in psw:
    if x in "1234567890":
        power[0]=1
    elif x in "abcdefghijklmnopqrstuvwxyz":
        power[1]=1
    elif x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        power[2]=1
    elif x in "~!@#$%^&*()_=-/,.?<>;{\:[}]|":
        power[4]=1
if len(psw)>=8:
    power[3]=1
print(power.count(1))

