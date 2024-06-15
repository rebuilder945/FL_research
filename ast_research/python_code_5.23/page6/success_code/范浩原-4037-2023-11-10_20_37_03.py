a=["3","4","5"]
b=["6","7","8"]
c=["9","10","11"]
d=["12","1","2"]
e=input()
m=0
if e in a:
    m="spring"
elif e in b:
    m="summer"
elif e in c :
    m="autumn"
elif e in d:
    m="winter"
else :
    m="error"
print(m)
