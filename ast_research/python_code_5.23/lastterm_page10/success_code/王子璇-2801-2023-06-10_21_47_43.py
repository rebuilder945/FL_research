n=input()
sum=0
lst=[]
lst1=[]
lst2=[]
lst3=[]
for x in n:
    if x.isnumeric():
        lst.append(x)
    if x.isupper():
        lst1.append(x)
    if x.islower():
        lst2.append(x)
    if x in ("~","!",'@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|',"\\"):
        lst3.append(x)
if lst!=[]:
    sum+=1
if lst1!=[]:
    sum+=1
if lst2!=[]:
    sum+=1
if lst3!=[]:
    sum+=1
if len(n)>=8:
    sum+=1
print(sum)

