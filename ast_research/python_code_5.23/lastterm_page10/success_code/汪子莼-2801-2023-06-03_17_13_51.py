n=input()
sum=0
lst=[]
lst1=[]
lst2=[]
lst3=[]
for x in n:
    if x.isdigit():
        lst.append(x)
    elif x.isupper():
        lst1.append(x)
    elif x.islower():
        lst2.append(x)
    elif x in ("~","!",'@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|',"\\"):
        lst3.append(x)
if lst!=[]:
    sum+=1
elif lst1!=[]:
    sum+=1
elif lst2!=[]:
    sum+=1
elif lst3!=[]:
    sum+=1
elif len(n)>8:
    sum+=1
print(sum)
