a=input()
e=0
shu=0
kong=0
teshu=0
for x in a:
    if ord("a")<=ord(x) and ord(x)<=ord("z") and ord("A")<=ord(x) and ord(x)<=ord("z"):
            e=e+1
    elif ord("0")<=ord(x)<=ord("9"):
          shu=shu+1
    elif x==" ":
          kong=kong+1
    else:
          teshu=teshu+1
print(e,kong,shu,teshu)
          
