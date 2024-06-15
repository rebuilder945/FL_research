s=input()
power=[0,0,0,0,0]
for i in s:
    if i.isdigit():
        power[0]=1
    if 'a'<=i<='z':
        power[1]=1
    if 'A'<=i<='Z':
        power[2]=1
    if i in '"~!@#$%^&*()_=-/,.?<>;:[]{}|\"':
        power[4]=1
if len(s)>=8:
    power[3]=1
print(power.count(1))
