passport=input()
p=list(passport)
x=0
count_number=0
count_alphbet=0
count_Alphbet=0
count_fuhao=0
for i in p:
    if "a"<=i<="z":
        count_alphbet+=1
    elif "A"<=i<="Z":
        count_Alphbet+=1
    elif "0"<=i<="9":
        count_number+=1
    else:
        count_fuhao+=1
if count_number!=0:
    x+=1
if count_alphbet!=0:
    x+=1
if count_Alphbet!=0:
    x+=1
if count_fuhao!=0:
    x+=1
if len(p)>=8:
    x+=1
print(x)
