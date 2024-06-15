PSW=input()
power=[0,0,0,0,0]
ls=["~","!","@","#","$","$","%","^","&","*","(",")","_","=","-","/",",",".","?","<",">",";",":","[","]","{","}","|","\\"]
for x in PSW:
    if "0"<=x<="9":
        power[0]=1
    if "a"<=x<="z":
        power[1]=1
    if "A"<=x<="Z":
        power[2]=1
    if x in ls:
        power[4]=1
if len(PSW)>=8:
    power[3]=1
print(power.count(1))

