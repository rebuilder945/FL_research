code=input()
star=0
l1=[]
l2=[]
l3=[]
l4=[]
if len(code)>=8:
        star+=1
for a in code:
    if a.isdigit():
        l1.append(a)
    if a.isupper():
        l2.append(a)
    if a.islower():
        l3.append(a)
    zifu=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',':',';','[',']','{','}','|',"\\"]
    if a in zifu:
        l4.append(a)
if l1!=[]:
    star+=1
if l2!=[]:
    star+=1
if l3!=[]:
    star+=1
if l4!=[]:
    star+=1
print(star)

