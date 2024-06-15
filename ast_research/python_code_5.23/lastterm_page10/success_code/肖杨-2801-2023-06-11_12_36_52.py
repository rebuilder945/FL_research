a=list(input())
j=0
for i in a:
    if i in '0123456789':
        j+=1
        break
for i in a:
    if i in 'qwertyuiopasdfghjklzxcvbnm':
        j+=1
        break
for i in a:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        j+=1
        break
if len(a)>7:
    j+=1
for i in a:
    if i in ["~","!","@","#","$","%","^","&","*","(",")","_","=","-","/",",",".","?","<",">",";",":","[","]","{","}","|"]:
        j+=1
        break
print(j)
             
             

