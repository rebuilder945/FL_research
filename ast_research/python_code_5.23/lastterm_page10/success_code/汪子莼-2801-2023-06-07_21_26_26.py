a=input()
sum=0
ls1=[]
ls2=[]
ls3=[]
ls4=[]
for x in a:
    if x.isdigit():   
        ls1.append(x)
    if x.islower():
        ls2.append(x)
    if x.isupper():
        ls3.append(x)
    if x in ("~","!",'@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|',"\\"):
        ls4.append(x)
if ls1!=[]:
    sum+=1
if ls2!=[]:
    sum+=1
if ls3!=[]:
    sum+=1
if ls4!=[]:
    sum+=1
if len(a)>=8:
    sum+=1
print(sum)
