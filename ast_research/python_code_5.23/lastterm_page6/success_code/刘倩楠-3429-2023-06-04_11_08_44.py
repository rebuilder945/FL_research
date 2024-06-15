s=input()
english=[]
a=0
b=0
c=0
number=[]
other=[]
d=0
for x in s:
    if str(0)<=x<=str(9):
        number.append(x)
        a=len(number)
    elif 'a'<=x<='z' or 'A'<=x<='Z':
        english.append(x)
        b=len(english)
    elif x==" ":
        c+=1
    else:
        other.append(x)
        d=len(other)
print(a,b,c,d)
