code=input()
n=0
lsnum=[]
lslow=[]
lsup=[]
lsstr=[]
for i in code:
    if i.isnumeric():
        lsnum.append(i)
    if i.islower():
        lslow.append(i)
    if i.isupper():
        lsup.append(i)
    if i in ('~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\'):
        lsstr.append(i)
if len(code)>=8:
    n+=1
if len(lsnum)!=0:
    n+=1
if len(lslow)!=0:
    n+=1
if len(lsup)!=0:
    n+=1
if len(lsstr)!=0:
    n+=1
print(n)
