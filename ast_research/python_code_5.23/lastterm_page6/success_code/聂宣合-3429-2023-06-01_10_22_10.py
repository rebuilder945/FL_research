stext=input()
eng=[]
spa=[]
num=[]
otr=[]
for i in stext:
    if i.isalpha() ==True:
        eng.append(i)
    elif i.isspace() ==True:
        spa.append(i)
    elif i.isalnum() ==True:
        num.append(i)
    else:
        otr.append(i)
print("%d %d %d %d"%(len(eng),len(spa),len(num),len(otr)))
