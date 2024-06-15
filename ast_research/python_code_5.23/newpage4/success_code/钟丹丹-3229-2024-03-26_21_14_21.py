from re import M


n = eval(input())
a=[]
b=[]
c=[]
j=""
for x in n:
    if n.count(x)>1:
        a.append(x)
    else:
        b.append(x)
if b==c:
    print("False")
else:
    b.sort()
    for x in b:
        j=j+str(x)+","
        j_winthout_last_comma=j.rstrip(',')
    print(j_winthout_last_comma)

