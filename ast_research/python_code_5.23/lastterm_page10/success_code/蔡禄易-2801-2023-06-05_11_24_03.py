a = input()
b = [x for x in a]
stars = 0
habi = ["~","!","@","#","$","%","^","&","*","()","_","=","-","/",",",".","?","<>",";",":","[]","{}","|","\""]
for i in b:
    if i.isalpha:
        if i.isupper:
            stars+=1
    break
for i in b:
    if i.isalpha:
        if i.islower:
            stars+=1
    break
for i in b:
    if i.isdigit:
        stars+=1
    break
for i in b:
    if i in habi:
        stars+=1
    break
if len(b) >= 8:
    stars+=1
print(stars)
