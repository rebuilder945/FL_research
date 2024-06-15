s=input().lower()
english=list(map(chr,range(97,123)))
a=[]
b=[]
x=0
for i in s:
    if i in english:
        a.append(i)
    elif ord(i) in range(48,58):
        b.append(i)
    elif i==" ":
        x+=1
c=[len(a),x,len(b),len(s)-len(a)-len(b)-x]
print(" ".join(map(str,c)))
