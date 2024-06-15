a = list(input())
l1=[]
l2=[]
l3=[]
l4=[]
for i in a:
    if ord("0")<=ord(i)<=ord("9"):
        l1.append(i)
    elif ord("a")<=ord(i)<=ord("z"):
        l2.append(i)
    elif ord("A")<=ord(i)<=ord("Z"):
        l3.append(i)
    elif i in ['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\']:
        l4.append(i)
c=5
if l1==[]:
    c-=1
if l2==[]:
    c-=1
if l3==[]:
    c-=1
if l4==[]:
    c-=1
if len(a)<8:
    c-=1
print(c)
