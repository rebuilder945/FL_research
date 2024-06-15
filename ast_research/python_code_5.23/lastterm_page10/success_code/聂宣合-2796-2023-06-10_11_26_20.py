stext=input()
text=""
final=[]
sums=[]
for i in stext:
    if i.isdigit():
        text+=i
    else:
        if text.isdigit():    
            final.append(text)
        text=""
if stext[-1].isdigit():
    final[-1]+=stext[-1]
b=0
for a in final:
    if len(a)>b:
        b=len(a)
for k in final:
    if len(k)==b:
        sums.append(k)

print(sums[-1])
